import datetime

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String

from models.database import Base


class BaekjoonUserInfo(Base):
    __tablename__ = "baekjoonUserInfo"

    id: Mapped[int] = mapped_column(primary_key=True)
    baekjoon_id: Mapped[str] = mapped_column(String(21), primary_key=True)

    baekjoon_tier: Mapped[int] = mapped_column(nullable=False)
    baekjoon_streak: Mapped[int] = mapped_column(default=0)
    baekjoon_level: Mapped[int] = mapped_column(nullable=False)

    solved_problem: Mapped[int] = mapped_column(nullable=False)
    tried_problem: Mapped[str] = mapped_column(String(length=21), nullable=False)

    session_joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())

    def __repr__(self):
        return (
            f"BaekjoonUserInfo(baekjoon_id={self.baekjoon_id!r}, "
            f"tier={self.baekjoon_tier!r}, "
            f"streak={self.baekjoon_streak!r} "
            f"session_joined_at={self.session_joined_at!r} "
            f"joined_at={self.joined_at!r})"
        )
