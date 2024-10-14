from fastapi_users.authentication import AuthenticationBackend, CookieTransport, JWTStrategy

from hosteypic_server.config import Config

cookie_transport = CookieTransport(
    cookie_name='hosteypic_token',
    cookie_max_age=86400,
    cookie_secure=False,
    cookie_httponly=True
)

def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=Config.SECRET_TOKEN, lifetime_seconds=86400)

auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
