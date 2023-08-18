from datetime import date as date_type

from sqlalchemy.dialects.postgresql import BIGINT, SMALLINT, VARCHAR, INTEGER, DATE, ARRAY
from sqlalchemy.orm import Mapped, mapped_column

from app.core import dto
from ..base import Base


class Day(Base):
    __tablename__ = "days"

    id: Mapped[int] = mapped_column(BIGINT(), primary_key=True)
    date: Mapped[date_type] = mapped_column(DATE())
    weekday: Mapped[int] = mapped_column(SMALLINT())
    lessons: Mapped[list[int]] = mapped_column(ARRAY(SMALLINT()))
    location: Mapped[str] = mapped_column(VARCHAR())

    def to_dto(self) -> dto.Day:
        return dto.Day(
            id=self.id,
            date=self.date,
            weekday=self.weekday,
            lessons=self.lessons,
            location=self.location
        )


class DefaultDay(Base):
    __tablename__ = "default_days"

    weekday: Mapped[int] = mapped_column(SMALLINT(), primary_key=True, autoincrement=False)
    lessons: Mapped[list[int]] = mapped_column(ARRAY(INTEGER()))
    location: Mapped[str] = mapped_column(VARCHAR())

    def to_dto(self) -> dto.DefaultDay:
        return dto.DefaultDay(
            weekday=self.weekday,
            lessons=self.lessons,
            location=self.location
        )
