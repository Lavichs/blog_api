from sqlalchemy.orm import Mapped, mapped_column

from database import BaseModel


class Post(BaseModel):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    content: Mapped[str]
    theme: Mapped[str]
