from datetime import datetime, date as date_type
from typing import List

from sqlalchemy.dialects.postgresql import BIGINT, TIMESTAMP, VARCHAR, INTEGER, DATE, ARRAY
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


class DayModel(Base):
    id: Mapped[int] = mapped_column(BIGINT(), primary_key=True)
    weekday: Mapped[int] = mapped_column(INTEGER())
    date: Mapped[date_type] = mapped_column(DATE())
    lessons: Mapped[List[int]] = mapped_column(ARRAY(INTEGER()))
    location: Mapped[str] = mapped_column(VARCHAR())


class DefaultDayModel(Base):
    weekday: Mapped[int] = mapped_column(INTEGER(), primary_key=True)
    lessons: Mapped[List[int]] = mapped_column(ARRAY(INTEGER()))
    location: Mapped[str] = mapped_column(VARCHAR())
