import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String

from models.database import Base


class BaekjoonUserInfo(Base):
    __tablename__ = "baekjoonUserInfo"

    baekjoon_id: Mapped[str] = mapped_column(String(21), primary_key=True)
    tier: Mapped[int] = mapped_column(nullable=False)
    streak: Mapped[int] = mapped_column(default=0)

    session_joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

    def __repr__(self):
        return (
            f"BaekjoonUserInfo(baekjoon_id={self.baekjoon_id!r}, "
            f"tier={self.tier!r}, "
            f"streak={self.streak!r} "
            f"session_joined_at={self.session_joined_at!r} "
            f"joined_at={self.joined_at!r})"
        )
