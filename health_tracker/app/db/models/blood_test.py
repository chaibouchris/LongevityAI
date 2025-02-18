from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

class BloodTest(Base):
    """
    Model representing a user's blood test results.
    """
    __tablename__ = "blood_tests"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    glucose_level = Column(Float, nullable=False)
    hemoglobin_level = Column(Float, nullable=False)
    cholesterol_level = Column(Float, nullable=False)
    creatinine_level = Column(Float, nullable=False)
    white_blood_cell_count = Column(Float, nullable=False)
    date = Column(Date, nullable=False)

    user = relationship("User", back_populates="blood_tests")