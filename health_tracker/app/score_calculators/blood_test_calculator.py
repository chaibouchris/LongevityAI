import logging
from sqlalchemy.orm import Session
from app.db.models import BloodTest
from app.utils.scoring import get_blood_ranges

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

blood_test_fields = {
    "glucose": "glucose_level",
    "hemoglobin": "hemoglobin_level",
    "cholesterol": "cholesterol_level",
    "creatinine": "creatinine_level",
    "wbc": "white_blood_cell_count"
}


def calculate_blood_test_score(user, db: Session):
    """
    Calculates the blood test score for a given user based on their latest blood test results.

    :param user: User object
    :param db: Database session
    :return: Tuple (total_score, explanations, individual_scores)
    """
    logging.info(f"Calculating blood test score for user ID {user.id}.")
    blood_test = db.query(BloodTest).filter(BloodTest.user_id == user.id).order_by(BloodTest.date.desc()).first()

    if not blood_test:
        logging.warning("No blood test data available for user.")
        return 0, ["No blood test data available."], {}

    total_score = 0
    explanations = []
    individual_scores = {}
    blood_ranges = get_blood_ranges(user.gender, user.age)

    for test, ranges in blood_ranges.items():
        field_name = blood_test_fields.get(test)
        value = getattr(blood_test, field_name, None)

        if value is not None:
            for min_val, max_val, score in ranges:
                if min_val <= value <= max_val:
                    total_score += score
                    individual_scores[test] = score
                    explanations.append(f"{test.capitalize()} level is {value} (Score: {score})")
                    break

    logging.info(f"Blood test score calculated: {total_score}")
    return total_score, explanations, individual_scores
