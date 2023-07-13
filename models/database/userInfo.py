import datetime

from models.database import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String


class UserInfo(Base):
    __tablename__ = "userInfo"

    id: Mapped[int] = mapped_column(primary_key=True)
    github_id: Mapped[str] = mapped_column(String(length=256), nullable=True)
    beakjoon_id: Mapped[str] = mapped_column(String(length=21), nullable=True)

    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

    experience: Mapped[int] = mapped_column(nullable=False, default=0)
    tier: Mapped[str] = mapped_column(String(length=128), nullable=False, default="unranked")
