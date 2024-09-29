from fastapi import FastAPI

from .test.router import router as router_test
# from .auth.router import router as router_auth

app = FastAPI(title='HosteyPic', root_path='/api')

app.include_router(router_test)
# app.include_router(router_auth)