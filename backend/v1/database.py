from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import create_engine, select, update, delete
from backend.v1.config import Config, get_config
from sqlalchemy.orm import Session

__all__ = (
    "new_user",
    "update_clicks",
    "get_clicks",
    "delete_user"
)

config: Config = get_config()

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    clicks: Mapped[int] = mapped_column(default=0)

    def __repr__(self):
        return f"Users(user_id={self.user_id!r}, clicks={self.clicks!r})"

engine = create_engine(f"postgresql://{config.db_user}:{config.db_password}@{config.db_url}")

Base.metadata.create_all(engine)


def new_user(user_id: int):
    with Session(engine) as session:
        user = User(
            user_id=user_id
        )

        session.add(user)
        session.commit()

def update_clicks(user_id: int, clicks: int):
    with Session(engine) as session:
        stmt = update(User).where(User.user_id == user_id).values(clicks=clicks)

        session.execute(stmt)
        session.commit()

def get_clicks(user_id: int) -> int:
    with Session(engine) as session:
        stmt = select(User.clicks).where(User.user_id == user_id)

        return session.scalar(stmt)

def delete_user(user_id: int):
    with Session(engine) as session:
        stmt = delete(User).where(User.user_id == user_id)

        session.execute(stmt)
        session.commit()
