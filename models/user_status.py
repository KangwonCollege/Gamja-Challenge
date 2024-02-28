from pydantic import BaseModel


class UserStatus(BaseModel):
    user_name: str
    user_level: int
    user_quest: list[int]
