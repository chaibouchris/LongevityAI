import logging


def calculate_stability_bonus(individual_scores):
    """
    Calculates a stability bonus based on the number of low scores.
    Users receive a bonus if they do not fail in any health metric.

    :param individual_scores: Dictionary of health metric scores
    :return: Tuple (bonus score, message)
    """
    logging.info("Calculating stability bonus.")
    num_low_scores = sum(1 for score in individual_scores.values() if score == 0)

    if num_low_scores == 0:
        logging.info("User passed all health metrics. Stability bonus awarded.")
        return 5, "Stability: You did not fail in any metric (Score: 5)"
    else:
        logging.info("User failed in one or more health metrics. No stability bonus.")
        return 0, None
