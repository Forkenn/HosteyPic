from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .auth.config import auth_backend
from .auth.manager import fastapi_users
from .auth.schemas import SUserRead, SUserCreate
from .auth.router import router as router_auth
from .users.router import router as router_users
from .posts.router import router as router_posts
from .likes.router import router as router_likes

app = FastAPI(title='HosteyPic', root_path='/api')

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://localhost:8080",    # VUE DEV URLs
    "http://127.0.0.1:8080",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://172.19.0.4",
    "http://127.0.0.1",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend), tags=["Auth"]
)

app.include_router(
    fastapi_users.get_register_router(SUserRead, SUserCreate),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_verify_router(SUserRead),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(router_auth)
app.include_router(router_users)
app.include_router(router_posts)
app.include_router(router_likes)
