from sqlalchemy.ext.asyncio import AsyncSession

from app.core.dao.models import User


class Database:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        self.user = User(session)

    async def commit(self) -> None:
        await self.session.commit()
