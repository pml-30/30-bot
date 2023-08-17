from typing import Any, Callable, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Update
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.core import dao


class DatabaseMiddleware(BaseMiddleware):
    def __init__(self, session_pool: async_sessionmaker) -> None:
        self._pool = session_pool

    async def __call__(
            self,
            handler: Callable[[Update, dict[str, Any]], Awaitable[Any]],
            event: Update,
            data: dict[str, Any]
    ) -> Any:
        async with self._pool() as session:
            data["db"] = dao.Database(session)
            return await handler(event, data)
