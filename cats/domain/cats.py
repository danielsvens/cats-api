from dataclasses import dataclass
from datetime import datetime

@dataclass
class Cat:
    name: str
    description: str

@dataclass
class ErrorMessage:
    status: int
    error: str
    message: str
    path: str
    timestamp: datetime
