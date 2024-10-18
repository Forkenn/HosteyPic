import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER = os.environ.get('DB_USER') or 'admin'
    DB_PASS = os.environ.get('DB_PASS') or 'my_super_password'
    DB_HOST = os.environ.get('DB_HOST') or 'localhost'
    DB_PORT = os.environ.get('DB_PORT') or 5432
    DB_NAME = os.environ.get('DB_NAME') or 'db_hosteypic'

    VERIFY_PATH = os.environ.get('VERIFY_PATH') or 'http://localhost/verify?token={token}'
    RESET_EMAIL_PATH = os.environ.get('VERIFY_PATH') or 'http://localhost/verify?token={token}&new_email={new_email}'

    SECRET_TOKEN = os.environ.get('SECRET_TOKEN') or 'dev_secret_key'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    COOKIE_NAME = "hosteypic_token"