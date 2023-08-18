from datetime import datetime

from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from app.core import dto
from ..base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BIGINT(), primary_key=True)
    tid: Mapped[int] = mapped_column(BIGINT(), unique=True)
    registration: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))

    def to_dto(self) -> dto.User:
        return dto.User(
            id=self.id,
            tid=self.tid,
            registration=self.registration
        )
