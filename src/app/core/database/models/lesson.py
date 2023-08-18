from sqlalchemy.dialects.postgresql import SMALLINT, VARCHAR
from sqlalchemy.orm import Mapped, mapped_column

from app.core import dto
from ..base import Base


class Lesson(Base):
    __tablename__ = "lessons"

    id: Mapped[int] = mapped_column(SMALLINT(), primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR())
    room: Mapped[str] = mapped_column(VARCHAR())
    teacher: Mapped[str] = mapped_column(VARCHAR())

    def to_dto(self) -> dto.Lesson:
        return dto.Lesson(
            id=self.id,
            name=self.name,
            room=self.room,
            teacher=self.teacher
        )
