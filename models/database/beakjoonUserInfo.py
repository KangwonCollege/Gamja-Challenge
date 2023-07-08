import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func

BASE = declarative_base()


class beakjoonUserInfo(BASE):
    __tablename__ = "beakjoonUserInfo"

    beakjoon_id: Mapped[str] = mapped_column(primary_key=True)
    tier: Mapped[int] = mapped_column(nullable=False)
    streak: Mapped[int] = mapped_column(default=0)

    session_joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
