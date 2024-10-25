import os
import random
import string
from tempfile import SpooledTemporaryFile
from pathlib import Path

class StorageManager():
    STORAGE_PATH = Path() / "uploads"

    @classmethod
    def delete_file(cls, filename: str, dir_path: Path) -> None:
        file = cls.STORAGE_PATH / dir_path / filename
        try:
            file.unlink()
        except Exception:
            return None

    @classmethod
    def save_file(
            cls,
            file: SpooledTemporaryFile,
            dir_path: Path,
            strict_filetype: str = None,
            strict_filename: str = None
    ) -> str:
        data = file.read()

        filename = strict_filename
        if not strict_filename:
            filename = ''.join(
                random.SystemRandom().choice(
                    string.ascii_lowercase + string.ascii_uppercase + string.digits
                ) for _ in range(30)
            )

        if strict_filetype:
            filename += '.' + strict_filetype

        save_to = cls.STORAGE_PATH / dir_path / filename
        os.makedirs(os.path.dirname(save_to), exist_ok=True)

        with open(save_to, "wb") as f:
            f.write(data)

        return filename
