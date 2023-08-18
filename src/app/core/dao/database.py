from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import dao


class Database:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user = dao.User(session)

    async def commit(self) -> None:
        await self.session.commit()
