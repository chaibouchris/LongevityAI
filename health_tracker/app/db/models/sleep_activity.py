from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class SleepActivity(Base):
    """
    Model representing a user's sleep activity.
    """
    __tablename__ = "sleep_activity"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    sleep_duration = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship("User", back_populates="sleeps")
