from typing import List
from tempfile import SpooledTemporaryFile
from pathlib import Path
from PIL import Image, ImageOps

from .config import Config
from .storage import StorageManager

class ImageManager():
    MIN_IMAGE_SIZE = Config.MIN_IMAGE_SIZE
    MAX_IMAGE_SIZE = Config.MAX_IMAGE_SIZE
    MIN_IMAGE_RATIO = Config.MIN_IMAGE_RATIO
    MAX_IMAGE_RATIO = Config.MAX_IMAGE_RATIO
    AVATAR_RATIO = Config.AVATAR_RATIO
    AVATAR_SIZES = Config.AVATAR_SIZES
    ATTACHMENT_SIZES = Config.ATTACHMENT_SIZES

    ORIG_AVATAR_PATH = Config.ORIG_AVATAR_PATH
    AVATAR_PATH = Config.AVATAR_PATH
    ORIG_ATTACHMENT_PATH = Config.ORIG_ATTACHMENT_PATH
    ATTACHMENT_PATH = Config.ATTACHMENT_PATH

    @classmethod
    def _validate_image(cls, image: Image.Image, strict_ratio: float = None) -> bool:
        aspect_ratio = image.width / image.height

        if not (
            cls.MIN_IMAGE_SIZE[0] <= image.width <= cls.MAX_IMAGE_SIZE[0] 
            or cls.MIN_IMAGE_SIZE[1] <= image.height <= cls.MAX_IMAGE_SIZE[1]
        ):
            return False
        
        if strict_ratio and aspect_ratio == strict_ratio:
            return True
        
        if not (cls.MIN_IMAGE_RATIO <= aspect_ratio <= cls.MAX_IMAGE_RATIO):
            return False
        
        return True
    
    @classmethod
    def _images_resize(cls, sizes: List[int], image: Image.Image) -> List[Image.Image]:
        images: List[Image.Image] = []
        for size in sizes:
            wpercent = (size / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))

            resized = image.resize((size, hsize), Image.Resampling.LANCZOS)
            images.append(resized)

        return images

    @classmethod
    def _save_image(cls, image_file: SpooledTemporaryFile, avatar: bool = False) -> str | None:
        image: Image.Image = Image.open(image_file).convert('RGB')
        image = ImageOps.exif_transpose(image)
        original_path = cls.ORIG_ATTACHMENT_PATH
        resize_path = cls.ATTACHMENT_PATH
        sizes = cls.ATTACHMENT_SIZES

        if avatar:
            original_path = cls.ORIG_AVATAR_PATH
            resize_path = cls.AVATAR_PATH
            sizes = cls.AVATAR_SIZES

        if not cls._validate_image(image, cls.AVATAR_RATIO if avatar else None):
            return None

        filename: str = None
        with SpooledTemporaryFile() as image_file:
            image.save(image_file, format="JPEG")
            image_file.seek(0)
            filename = StorageManager.save_file(
                image_file, Path(original_path), strict_filetype='jpg'
            )

        if not filename:
            return None

        resized_images: list[Image.Image] = cls._images_resize(sizes, image)
        for resized_image in resized_images:
            with SpooledTemporaryFile() as image_file:
                resized_image.save(image_file, format="JPEG")
                image_file.seek(0)
                StorageManager.save_file(
                    image_file,
                    Path(resize_path.format(img_size=resized_image.size[0])),
                    strict_filename=filename
                )

        image.close()
        return filename
    
    @classmethod
    def _delete_image(cls, filename: str, avatar: bool = False) -> None:
        original_path = cls.ORIG_ATTACHMENT_PATH
        resize_path = cls.ATTACHMENT_PATH
        sizes = cls.ATTACHMENT_SIZES

        if avatar:
            original_path = cls.ORIG_AVATAR_PATH
            resize_path = cls.AVATAR_PATH
            sizes = cls.AVATAR_SIZES

        for size in sizes:
            StorageManager.delete_file(
                filename,
                Path(resize_path.format(img_size=size))
            )

        StorageManager.delete_file(filename, Path(original_path))
    
    @classmethod
    def upload_avatar(cls, image_file: SpooledTemporaryFile) -> str | None:
        return cls._save_image(image_file, True)
    
    @classmethod
    def delete_avatar(cls, filename) -> None:
        cls._delete_image(filename, True)

    @classmethod
    def upload_attachment(cls, image_file: SpooledTemporaryFile) -> str | None:
        return cls._save_image(image_file)

    @classmethod
    def delete_attachment(cls, filename):
        cls._delete_image(filename)
