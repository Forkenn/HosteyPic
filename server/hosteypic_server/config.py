import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.environ.get('DB_USER') or 'admin'
    DB_PASS = os.environ.get('DB_PASS') or 'my_super_password'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or 5432
    DB_NAME = os.environ.get('DB_NAME') or 'db_hosteypic'

    SECRET_TOKEN = os.environ.get('SECRET_TOKEN') or 'dev_secret_key'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    COOKIE_NAME = "hosteypic_token"

    VERIFY_URL = os.environ.get('VERIFY_PATH') or 'http://localhost/verify?token={token}'
    CHANGE_EMAIL_URL = os.environ.get('CHANGE_EMAIL_URL') or 'http://localhost/change-email?token={token}&new_email={new_email}'
    RESET_URL = os.environ.get('RESET_URL') or 'http://localhost/reset-password?token={token}'

    MIN_IMAGE_SIZE = (256, 256)
    MAX_IMAGE_SIZE = (4000, 4000)
    MIN_IMAGE_RATIO = 0.45
    MAX_IMAGE_RATIO = 2
    AVATAR_SIZES = [52, 128, 200, 256]
    ATTACHMENT_SIZES = [256, 362, 420, 512]

    MAX_TAGS_COUNT = 100
