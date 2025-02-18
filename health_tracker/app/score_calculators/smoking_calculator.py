import logging


def get_smoking_penalty(smoking_habits):
    """
    Returns the penalty score based on smoking habits.

    :param smoking_habits: Integer representing smoking frequency
    :return: Penalty score (negative or zero)
    """
    logging.info("Calculating smoking penalty.")
    penalties = {
        0: 0,  # Non-smoker ✅ 0 pts
        1: -5,  # Occasional smoker ⚠️ -5 pts
        2: -10  # Regular smoker 🚨 -10 pts
    }
    penalty = penalties.get(smoking_habits, 0)
    logging.info(f"Smoking habit: {smoking_habits}, Penalty: {penalty}")
    return penalty