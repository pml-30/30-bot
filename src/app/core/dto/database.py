from dataclasses import dataclass
from datetime import datetime, date as date_type


@dataclass
class UserDTO:
    uid: int
    tid: int
    registration: datetime


@dataclass
class LessonDTO:
    id: int
    name: str
    room: int
    teacher: str

@dataclass
class DefaultDayDTO:
    weekday: int
    lessons: list[LessonDTO]
    location: str

@dataclass
class DayDTO(DefaultDayDTO):
    id: int
    date: date_type
