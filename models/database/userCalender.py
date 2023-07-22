import datetime

import sqlalchemy

from models.database import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String, JSON


class UserCalender(Base):
    __tablename__ = "userCalender"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    github_id: Mapped[str] = mapped_column(String(length=256), nullable=True)
    baekjoon_id: Mapped[str] = mapped_column(String(length=21), nullable=True)

    streak: Mapped[int] = mapped_column(default=0)
    session_joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

    calender_cnt: Mapped[JSON] = mapped_column(JSON)
