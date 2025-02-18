import logging
from sqlalchemy.orm import Session
from app.db.models import SleepActivity
from app.utils.scoring import get_sleep_ranges


def calculate_sleep_score(user, db: Session):
    """
    Calculates the sleep score for a given user based on their recorded sleep activity.

    :param user: User object
    :param db: Database session
    :return: Tuple (total_score, explanations, individual_scores)
    """
    logging.info(f"Calculating sleep score for user ID {user.id}.")
    sleep = db.query(SleepActivity).filter(SleepActivity.user_id == user.id).order_by(SleepActivity.date.desc()).first()

    if not sleep:
        logging.warning("No sleep data available for user.")
        return 0, ["No sleep data available."], {}

    sleep_ranges = get_sleep_ranges(user.age)["sleep"]
    total_score = 0
    explanations = []
    individual_scores = {}

    for min_val, max_val, score in sleep_ranges:
        if min_val <= sleep.sleep_duration <= max_val:
            total_score += score
            individual_scores["sleep"] = score
            explanations.append(f"Sleep hours: {sleep.sleep_duration} (Score: {score})")
            break

    logging.info(f"Sleep score calculated: {total_score}")
    return total_score, explanations, individual_scores
