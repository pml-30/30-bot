from dataclasses import dataclass
from datetime import datetime, date as date_type


@dataclass
class User:
    id: int
    tid: int
    registration: datetime


@dataclass
class Lesson:
    id: int
    name: str
    room: str
    teacher: str


@dataclass
class DefaultDay:
    weekday: int
    lessons: list[int]
    location: str


@dataclass
class Day(DefaultDay):
    id: int
    date: date_type
