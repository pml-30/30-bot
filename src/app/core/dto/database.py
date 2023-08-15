from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDTO:
    uid: int
    tid: int
    registration: datetime
