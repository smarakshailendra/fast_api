from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    name: str
    age: Optional[str] = None
    email: float
    role: Optional[float] = None