from typing import AsyncGenerator
from sqlalchemy import insert, select, delete, update, Integer, inspect, String, ForeignKey
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, declared_attr
from config import DB_USER, DB_PASS, DB_PORT, DB_NAME, DB_HOST


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class Base(DeclarativeBase):
    pass


class Bot(Base):
    __tablename__ = "bot"

    id: Mapped[int] = mapped_column(primary_key=True)


class Group(Base):
    __tablename__ = "group"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    @declared_attr
    def bot_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("bot.id", ondelete="cascade"), nullable=True)


class Method(Base):
    __tablename__ = "method"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()

    @declared_attr
    def bot_id(cls) -> Mapped[int]:
        return mapped_column(ForeignKey("bot.id", ondelete="cascade"), nullable=True)


async_engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
