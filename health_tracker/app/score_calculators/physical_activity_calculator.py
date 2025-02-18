import logging
from sqlalchemy.orm import Session
from app.db.models import PhysicalActivity
from app.utils.scoring import get_step_ranges


def calculate_physical_activity_score(user, db: Session):
    """
    Calculates the physical activity score for a given user based on their recorded step count.

    :param user: User object
    :param db: Database session
    :return: Tuple (total_score, explanations, individual_scores)
    """
    logging.info(f"Calculating physical activity score for user ID {user.id}.")
    steps = db.query(PhysicalActivity).filter(PhysicalActivity.user_id == user.id).order_by(
        PhysicalActivity.date.desc()).first()

    if not steps:
        logging.warning("No physical activity data available for user.")
        return 0, ["No physical activity data available."], {}

    step_ranges = get_step_ranges(user.age)["steps"]
    total_score = 0
    explanations = []
    individual_scores = {}

    for min_val, max_val, score in step_ranges:
        if min_val <= steps.steps <= max_val:
            total_score += score
            individual_scores["steps"] = score
            explanations.append(f"Step count: {steps.steps} (Score: {score})")
            break

    logging.info(f"Physical activity score calculated: {total_score}")
    return total_score, explanations, individual_scores
