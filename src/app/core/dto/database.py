from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserDTO:
    tid: int
    registration: datetime
