from datetime import datetime

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core import dto
from src.app.core.database import models


class User:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_one(self, tid: int) -> dto.User | None:
        stmt = select(models.User).where(models.User.tid == tid)
        result: models.User | None = await self.session.scalar(stmt)
        return None if result is None else (
            dto.User(uid=result.uid, tid=result.tid, registration=result.registration)
        )

    async def add_one(self, tid: int, registration: datetime) -> int | None:
        stmt = select(models.User.tid).where(models.User.tid == tid)
        result: int | None = await self.session.scalar(stmt)

        if result is None:
            stmt = insert(models.User).values(tid=tid, registration=registration).returning(models.User.uid)
            result: int = await self.session.scalar(stmt)
            return result

        return None
