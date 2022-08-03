from typing import List, Optional
from pydantic import BaseModel
from .types import RoleType


class User(BaseModel):
    id: int
    name: str
    email: str
    birth_day: str
    preferred_days: list[str]
    roles: Optional[list[RoleType]]
