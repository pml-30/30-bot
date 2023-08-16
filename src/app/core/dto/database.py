from dataclasses import dataclass
from datetime import datetime


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
    location: str
