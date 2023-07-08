import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

BASE = declarative_base()


class UserInfo(BASE):
    __tablename__ = "userInfo"

    id: Mapped[int] = mapped_column(primary_key=True)
    github_id: Mapped[str] = mapped_column(nullable=True)
    beakjoon_id: Mapped[str] = mapped_column(nullable=True)

    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

    experience: Mapped[int] = mapped_column(nullable=False, default=0)
    tier: Mapped[str] = mapped_column(nullable=False, default="unranked")
