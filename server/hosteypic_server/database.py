from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from hosteypic_server.config import Config

DB_USER = Config.DB_USER
DB_PASS = Config.DB_PASS
DB_HOST = Config.DB_HOST
DB_PORT = Config.DB_PORT
DB_NAME = Config.DB_NAME

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

Base: DeclarativeMeta = declarative_base()

engine = create_async_engine(DATABASE_URL, pool_size=100, max_overflow=0)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
