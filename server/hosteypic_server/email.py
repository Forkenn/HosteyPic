import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from hosteypic_server.config import Config

class EmailManager:
    if not Config.DEBUG:
        MAIL_HOST = Config.MAIL_HOST
        MAIL_PORT = Config.MAIL_PORT
        MAIL_USE_TLS = Config.MAIL_USE_TLS
        MAIL_USE_SSL = Config.MAIL_USE_SSL
        MAIL_DEFAULT_SENDER = Config.MAIL_DEFAULT_SENDER

    @classmethod
    async def send_email(cls, subject: str, recipient: str, text_body: str):
        if Config.DEBUG:
            print(text_body)
            return

        msg = MIMEMultipart()
        msg['From'] = cls.MAIL_DEFAULT_SENDER
        msg['To'] = recipient
        msg['Subject'] = subject
        msg.attach(MIMEText(text_body, 'plain'))

        with smtplib.SMTP(cls.MAIL_HOST, cls.MAIL_PORT) as server:
            server.sendmail(cls.MAIL_DEFAULT_SENDER, recipient, msg.as_string())
