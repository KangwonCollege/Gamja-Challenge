import datetime

from models.database import Base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.sql import func
from sqlalchemy import String


class GithubUserInfo(Base):
    __tablename__ = "githubUserInfo"

    github_ids: Mapped[str] = mapped_column(String(length=256), primary_key=True)
    commit_count: Mapped[int] = mapped_column(default=0)

    joined_at: Mapped[datetime.datetime] = mapped_column(default=func.now())
