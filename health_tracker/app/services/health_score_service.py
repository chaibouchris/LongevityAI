import logging
from sqlalchemy.orm import Session
from app.db.models import User, HealthScore
from app.score_calculators.blood_test_calculator import calculate_blood_test_score
from app.score_calculators.physical_activity_calculator import calculate_physical_activity_score
from app.score_calculators.sleep_calculator import calculate_sleep_score
from app.score_calculators.stability_calculator import calculate_stability_bonus
from app.score_calculators.bmi_calculator import calculate_bmi_score
from app.score_calculators.averege_comparison_calculator import get_comparison_score
from app.score_calculators.smoking_calculator import get_smoking_penalty
from app.services.system_health_average_service import get_latest_system_average

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_health_score(user_id: int, db: Session):
    """
    Calculates the health score for a given user based on various health metrics.
    """
    logging.info(f"Calculating health score for user ID {user_id}.")
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        logging.warning(f"User with ID {user_id} not found.")
        raise ValueError("User not found")

    total_score = 0
    explanations = []
    individual_scores = {}

    # Calculate individual scores
    blood_score, blood_explanations, blood_scores = calculate_blood_test_score(user, db)
    step_score, step_explanations, step_scores = calculate_physical_activity_score(user, db)
    sleep_score, sleep_explanations, sleep_scores = calculate_sleep_score(user, db)
    bmi_score, bmi_explanation = calculate_bmi_score(user.weight, user.height)

    # Aggregate scores
    total_score += blood_score + step_score + sleep_score + bmi_score
    individual_scores.update(blood_scores)
    individual_scores.update(step_scores)
    individual_scores.update(sleep_scores)
    explanations.append(bmi_explanation)
    explanations.extend(blood_explanations + step_explanations + sleep_explanations)


    # Stability bonus
    stability_bonus, stability_message = calculate_stability_bonus(individual_scores)
    total_score += stability_bonus
    if stability_message:
        explanations.append(stability_message)

    # Smoking penalty
    smoking_penalty = get_smoking_penalty(user.smoking_habits)
    total_score += smoking_penalty
    if smoking_penalty < 0:
        explanations.append(f"Smoking habit penalty: {smoking_penalty}")

    # System average comparison
    system_avg = get_latest_system_average(db)
    comparison_bonus, comparison_message = get_comparison_score(total_score, system_avg)
    total_score += comparison_bonus
    if comparison_message:
        explanations.append(comparison_message)

    # Ensure score stays within valid range
    total_score = max(0, min(100, total_score))
    logging.info(f"Final health score for user {user_id}: {total_score}")

    # Update health score record
    health_score_entry = db.query(HealthScore).filter(HealthScore.user_id == user_id).first()
    if health_score_entry:
        health_score_entry.score = total_score
    else:
        db.add(HealthScore(user_id=user_id, score=total_score))

    db.commit()

    return {"user_id": user_id, "health_score": total_score, "details": explanations}
