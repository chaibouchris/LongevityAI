import logging


def calculate_bmi_score(weight, height):
    """
    Calculates the BMI score based on weight and height.

    :param weight: User's weight in kg
    :param height: User's height in meters
    :return: Tuple (score, explanation)
    """
    if not weight or not height or height == 0:
        logging.warning("BMI data unavailable.")
        return 0, "BMI data unavailable."

    bmi = weight / (height ** 2)
    logging.info(f"Calculated BMI: {bmi:.1f}")

    if bmi < 16:
        return 0, f"BMI is {bmi:.1f} (Severely Underweight, Score: 0)"
    elif 16 <= bmi < 17:
        return 5, f"BMI is {bmi:.1f} (Moderately Underweight, Score: 5)"
    elif 17 <= bmi < 18.5:
        return 10, f"BMI is {bmi:.1f} (Mildly Underweight, Score: 10)"
    elif 18.5 <= bmi <= 24.9:
        return 20, f"BMI is {bmi:.1f} (Healthy range, Score: 20)"
    elif 25 <= bmi <= 29.9:
        return 15, f"BMI is {bmi:.1f} (Overweight, Score: 15)"
    elif 30 <= bmi <= 34.9:
        return 10, f"BMI is {bmi:.1f} (Obese Class I, Score: 10)"
    elif 35 <= bmi <= 39.9:
        return 5, f"BMI is {bmi:.1f} (Obese Class II, Score: 5)"
    else:
        return 0, f"BMI is {bmi:.1f} (Severely Obese, Score: 0)"