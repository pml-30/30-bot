from sqlalchemy.ext.asyncio import AsyncSession

from .user import UserDAO


class DatabaseDAO:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user = UserDAO(session)

    async def commit(self) -> None:
        await self.session.commit()
