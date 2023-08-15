from datetime import datetime

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.app.core.database import UserModel
from src.app.core.dto import UserDTO


class UserDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def get_one(self, tid: int) -> UserDTO | None:
        stmt = select(UserModel).where(UserModel.tid == tid)
        result: UserModel | None = await self.session.scalar(stmt)
        return None if result is None else (
            UserDTO(uid=result.uid, tid=result.tid, registration=result.registration)
        )

    async def add_one(self, tid: int, registration: datetime) -> int | None:
        stmt = select(UserModel.tid).where(UserModel.tid == tid)
        result: int | None = await self.session.scalar(stmt)

        if result is None:
            stmt = insert(UserModel).values(tid=tid, registration=registration).returning(UserModel.uid)
            result: int = await self.session.scalar(stmt)
            return result

        return None
