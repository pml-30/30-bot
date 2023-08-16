from datetime import datetime

from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class UserModel(Base):
    uid: Mapped[int] = mapped_column(BIGINT(), primary_key=True)
    tid: Mapped[int] = mapped_column(BIGINT(), unique=True)
    registration: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True))


class LessonModel(Base):
    id: Mapped[int] = mapped_column(BIGINT(), primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR())
    room: Mapped[int] = mapped_column(VARCHAR())
    teacher: Mapped[str] = mapped_column(VARCHAR())
    location: Mapped[str] = mapped_column(VARCHAR())

