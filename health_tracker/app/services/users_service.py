import logging
from sqlalchemy.orm import Session
from app.db.models import User, GenderEnum, SmokingEnum
from fastapi import HTTPException

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_all_users(db: Session):
    """
    Retrieves all users from the database.
    """
    logging.info("Fetching all users from the database.")
    return db.query(User).all()

def get_user_by_id(user_id: int, db: Session):
    """
    Retrieves a specific user by their ID.
    """
    logging.info(f"Fetching user with ID {user_id}.")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.warning(f"User with ID {user_id} not found.")
        raise HTTPException(status_code=404, detail="User not found")
    return user

def create_user(user_data, db: Session):
    """
    Creates a new user in the database.
    """
    logging.info(f"Creating new user: {user_data.email}")
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        logging.warning(f"Attempt to create user with existing email: {user_data.email}")
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(
        name=user_data.name,
        email=user_data.email,
        gender=GenderEnum(user_data.gender),
        age=user_data.age,
        smoking_habits=SmokingEnum(user_data.smoking_habits) if user_data.smoking_habits is not None else None,
        weight=user_data.weight,
        height=user_data.height
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logging.info(f"User created successfully: {user_data.email}")
    return new_user

def update_user(user_id: int, updated_data, db: Session):
    """
    Updates user details by ID.
    """
    logging.info(f"Updating user with ID {user_id}.")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.warning(f"User with ID {user_id} not found for update.")
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_data.name
    user.email = updated_data.email
    user.gender = GenderEnum(updated_data.gender)
    user.age = updated_data.age
    user.smoking_habits = SmokingEnum(updated_data.smoking_habits) if updated_data.smoking_habits is not None else None
    user.weight = updated_data.weight
    user.height = updated_data.height

    db.commit()
    db.refresh(user)
    logging.info(f"User with ID {user_id} updated successfully.")
    return user

def delete_user(user_id: int, db: Session):
    """
    Deletes a user by ID.
    """
    logging.info(f"Deleting user with ID {user_id}.")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.warning(f"User with ID {user_id} not found for deletion.")
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()
    logging.info(f"User with ID {user_id} deleted successfully.")
    return {"message": "User deleted successfully"}
