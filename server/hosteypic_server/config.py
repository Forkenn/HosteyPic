import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = os.environ.get('DEBUG') or True

    DB_USER = os.environ.get('DB_USER') or 'admin'
    DB_PASS = os.environ.get('DB_PASS') or 'my_super_password'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or 5432
    DB_NAME = os.environ.get('DB_NAME') or 'db_hosteypic'

    SECRET_TOKEN = os.environ.get('SECRET_TOKEN') or 'dev_secret_key'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    COOKIE_NAME = "hosteypic_token"

    FRONTEND_URL = os.environ.get('FRONTEND_URL') or 'http://localhost/'
    VERIFY_URL = FRONTEND_URL + 'verify?token={token}'
    CHANGE_EMAIL_URL = FRONTEND_URL + 'change-email?token={token}&new_email={new_email}'
    RESET_URL = FRONTEND_URL + 'reset-password?token={token}'

    MAIL_HOST = os.environ.get('MAIL_HOST') or 'localhost'
    MAIL_PORT = os.environ.get('MAIL_PORT') or 25
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') or False
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL') or False
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER') or 'noreply@example.com'
    MAIL_DOMAIN = os.environ.get('MAIL_DOMAIN') or 'example.com'

    MIN_IMAGE_SIZE = (256, 256)
    MAX_IMAGE_SIZE = (4000, 4000)
    MIN_IMAGE_RATIO = 0.45
    MAX_IMAGE_RATIO = 2
    AVATAR_SIZES = [52, 128, 200, 256]
    ATTACHMENT_SIZES = [256, 362, 420, 512]

    MAX_TAGS_COUNT = 100
