from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

BASE = declarative_base()


class beakjoonInfo(BASE):
    __tablename__ = "beakjoonInfo"

    beakjoon_id: Mapped[str] = mapped_column(primary_key=True)
    tier: Mapped[str] = mapped_column(nullable=False)
    streak: Mapped[int] = mapped_column()
    solved