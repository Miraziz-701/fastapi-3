from fastapi import Depends
from typing import Annotated
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from config import DATABASE_URL


engine = create_async_engine(DATABASE_URL)

new_session = async_sessionmaker(engine, expire_on_commit=True)

async def get_session():
    async with new_session() as session:
        yield session


DepSession = Annotated[AsyncSession, Depends(get_session)]

Base = declarative_base()


async def init_models():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)