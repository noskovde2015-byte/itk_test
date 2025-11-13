from sqlalchemy.orm import Mapped

from core.models import Base


class User(Base):
    __tablename__ = 'users'
    name: Mapped[str]
    surname: Mapped[str]
    age: Mapped[int]
    email: Mapped[str]