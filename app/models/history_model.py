from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship











    owner: Mapped[User] = relationship("User", back_populates="history")  