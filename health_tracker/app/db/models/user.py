from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from app.db.database import Base
import enum

# Enum for Gender
class GenderEnum(enum.IntEnum):
    male = 1
    female = 2

# Enum for Smoking Habits
class SmokingEnum(enum.IntEnum):
    non_smoker = 0
    occasional = 1
    heavy_smoker = 2

class User(Base):
    """
    User model representing a user in the system.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    gender = Column(Integer, nullable=False)
    age = Column(Integer, nullable=False)
    smoking_habits = Column(Integer, nullable=True)
    weight = Column(Float, nullable=True)
    height = Column(Float, nullable=True)

    activities = relationship("PhysicalActivity", back_populates="user")
    sleeps = relationship("SleepActivity", back_populates="user")
    blood_tests = relationship("BloodTest", back_populates="user")
