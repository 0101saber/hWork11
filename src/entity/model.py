from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from src.database.db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(13))
    born_date: Mapped[str] = mapped_column(Date())
    delete: Mapped[bool] = mapped_column(default=False)
