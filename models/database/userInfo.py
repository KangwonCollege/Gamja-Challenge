import datetime

from models.database import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String, JSON


class UserInfo(Base):
    __tablename__ = "userInfo"

    id: Mapped[int] = mapped_column(primary_key=True)
    baekjoon_id: Mapped[str] = mapped_column(String(length=21), nullable=True)

    experience: Mapped[int] = mapped_column(nullable=False, default=0)
    tier: Mapped[str] = mapped_column(String(length=21), nullable=False, default="unranked")

    github_commit: Mapped[int] = mapped_column(nullable=True)
    baekjoon_solved: Mapped[int] = mapped_column(nullable=True)

    calender_cnt: Mapped[JSON] = mapped_column(JSON)

    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

