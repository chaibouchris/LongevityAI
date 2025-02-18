import logging


def get_comparison_score(user_score, system_avg):
    """
    Compares the user's health score with the system average and assigns a score accordingly.

    :param user_score: User's health score
    :param system_avg: System-wide average health score
    :return: Tuple (bonus score, message)
    """
    logging.info(f"Comparing user score {user_score} with system average {system_avg}.")
    adjusted_avg = system_avg * 0.9

    if user_score >= adjusted_avg:
        logging.info("User score is at or above adjusted system average. Bonus awarded.")
        return 10, "At or above adjusted system average (Score: 10)"
    else:
        logging.warning("User score is below adjusted system average. No bonus awarded.")
        return 0, "Below adjusted system average (Score: 0)"
