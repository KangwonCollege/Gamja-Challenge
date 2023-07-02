from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

BASE = declarative_base()


class BeakjoonProblem(BASE):
    __tablename__ = "beakjoonProblem"

    problem_id: Mapped[str] = mapped_column(primary_key=True)
    problem_name: Mapped[str] = mapped_column(nullable=False)
    tier: Mapped[str] = mapped_column(nullable=False)
