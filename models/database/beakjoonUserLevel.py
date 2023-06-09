
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String

from models.database import Base
from modules.enum import BeakjoonUserLevelType


class BeakjoonUserLevel(Base):
    __tablename__ = "beakjoonUserLevel"

    beakjoon_id: Mapped[str] = mapped_column(String(length=21), primary_key=True)
    level: Mapped[int] = mapped_column(nullable=False)
    percent: Mapped[float] = mapped_column(nullable=False)
    sovled_problem: Mapped[int] = mapped_column(nullable=False)
    tried_problem: Mapped[int] = mapped_column(nullable=False)
    type: Mapped[BeakjoonUserLevelType] = mapped_column(nullable=False)
