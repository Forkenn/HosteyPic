from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .test.router import router as router_test
# from .auth.router import router as router_auth

app = FastAPI(title='HosteyPic', root_path='/api')

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
    "http://127.0.0.1",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router_test)
# app.include_router(router_auth)