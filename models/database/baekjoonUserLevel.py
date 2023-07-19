
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from models.database import Base
from modules.enum import BaekjoonUserLevelType


class BaekjoonUserLevel(Base):
    __tablename__ = "baekjoonUserLevel"

    baekjoon_id: Mapped[str] = mapped_column(String(length=21), primary_key=True)
    level: Mapped[int] = mapped_column(nullable=False)
    percent: Mapped[float] = mapped_column(nullable=False)
    sovled_problem: Mapped[int] = mapped_column(nullable=False)
    tried_problem: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[BaekjoonUserLevelType] = mapped_column(nullable=False)
