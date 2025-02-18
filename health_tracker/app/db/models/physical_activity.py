from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.database import Base

class PhysicalActivity(Base):
    """
    Model representing a user's physical activity.
    """
    __tablename__ = "physical_activity"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    steps = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship("User", back_populates="activities")