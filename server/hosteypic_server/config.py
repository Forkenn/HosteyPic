import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DEBUG = int(os.environ.get('DEBUG'))
    STRICT_MODE = int(os.environ.get('STRICT_MODE'))

    DB_USER = os.environ.get('DB_USER')
    DB_PASS = os.environ.get('DB_PASS')
    DB_HOST = os.environ.get('DB_HOST')
    DB_PORT = os.environ.get('DB_PORT')
    DB_NAME = os.environ.get('DB_NAME')

    SECRET_TOKEN = os.environ.get('SECRET_TOKEN')
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    COOKIE_NAME = "hosteypic_token"

    FRONTEND_URL = os.environ.get('FRONTEND_URL')
    VERIFY_URL = FRONTEND_URL + 'verify?token={token}'
    CHANGE_EMAIL_URL = FRONTEND_URL + 'change-email?token={token}&new_email={new_email}'
    RESET_URL = FRONTEND_URL + 'reset-password?token={token}'

    MAIL_HOST = os.environ.get('MAIL_HOST')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = int(os.environ.get('MAIL_USE_TLS'))
    MAIL_USE_SSL = int(os.environ.get('MAIL_USE_SSL'))
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_DOMAIN = os.environ.get('MAIL_DOMAIN')

    MIN_IMAGE_SIZE = (256, 256)
    MAX_IMAGE_SIZE = (4000, 4000)
    MIN_IMAGE_RATIO = 0.45
    MAX_IMAGE_RATIO = 2
    AVATAR_SIZES = [52, 128, 200, 256]
    ATTACHMENT_SIZES = [256, 362, 420, 512]

    MAX_TAGS_COUNT = 100
