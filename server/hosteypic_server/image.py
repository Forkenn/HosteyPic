from typing import List
from tempfile import SpooledTemporaryFile
from pathlib import Path
from PIL import Image

from .config import Config
from .storage import StorageManager

class ImageManager():
    MIN_IMAGE_SIZE = Config.MIN_IMAGE_SIZE
    MAX_IMAGE_SIZE = Config.MAX_IMAGE_SIZE
    MIN_IMAGE_RATIO = Config.MIN_IMAGE_RATIO
    MAX_IMAGE_RATIO = Config.MAX_IMAGE_RATIO
    AVATAR_SIZES = Config.AVATAR_SIZES
    ATTACHMENT_SIZES = Config.ATTACHMENT_SIZES

    @classmethod
    def _validate_image(cls, image: Image.Image, strict_ratio: float = None) -> bool:
        aspect_ratio = image.width/image.height

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
        
    def _images_resize(sizes: List[int], image: Image.Image) -> List[Image.Image]:
        images: List[Image.Image] = []
        for size in sizes:
            wpercent = (size / float(image.size[0]))
            hsize = int((float(image.size[1]) * float(wpercent)))

            resized = image.resize((size, hsize), Image.Resampling.LANCZOS)
            images.append(resized)

        return images
    
    @classmethod
    def upload_avatar(cls, image_file: SpooledTemporaryFile) -> str | None:
        image: Image.Image = Image.open(image_file).convert('RGB')

        if not cls._validate_image(image, 1.0):
            return None

        filename: str = None
        with SpooledTemporaryFile() as image_file:
            image.save(image_file, format="JPEG")
            image_file.seek(0)
            filename = StorageManager.save_file(
                image_file, Path('avatars/original'), strict_filetype='jpg'
            )

        if not filename:
            return None

        resized_images: List[Image.Image] = cls._images_resize(cls.AVATAR_SIZES, image)
        for resized_image in resized_images:
            with SpooledTemporaryFile() as image_file:              # TODO: EDIT TYPE
                resized_image.save(image_file, format="JPEG")
                image_file.seek(0)
                StorageManager.save_file(
                    image_file, Path(f'avatars/{resized_image.size[0]}x'), strict_filename=filename
                )

        return filename
    
    @classmethod
    def delete_avatar(cls, filename) -> None:
        for size in cls.AVATAR_SIZES:
            StorageManager.delete_file(filename, Path(f'avatars/{size}x'))

        StorageManager.delete_file(filename, Path(f'avatars/original'))

    @classmethod
    def upload_attachment(image: SpooledTemporaryFile):
        pass