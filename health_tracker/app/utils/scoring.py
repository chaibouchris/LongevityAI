import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_blood_ranges(gender, age):
    """
    Returns blood parameter score ranges based on gender and age.
    """
    return {
        "glucose": [
            (0, 59, 0), (60, 69, 5), (70, 99, 10), (100, 125, 5), (126, float('inf'), 0)
        ] if age <= 40 else [
            (0, 59, 0), (60, 69, 5), (70, 105, 10), (106, 125, 5), (126, float('inf'), 0)
        ] if age <= 60 else [
            (0, 59, 0), (60, 69, 5), (70, 110, 10), (111, 130, 5), (131, float('inf'), 0)
        ],
        "hemoglobin": [
            (0, 8.9, 0), (9, 12.7, 5), (12.8, 17.2, 10), (17.3, float('inf'), 5)
        ] if gender == "male" else [
            (0, 8.9, 0), (9, 11.9, 5), (12, 15.1, 10), (15.2, float('inf'), 5)
        ],
        "cholesterol": [
            (0, 149, 5), (150, 200, 10), (201, 239, 5), (240, float('inf'), 0)
        ] if age <= 40 else [
            (0, 149, 5), (150, 210, 10), (211, 249, 5), (250, float('inf'), 0)
        ] if age <= 60 else [
            (0, 149, 5), (150, 220, 10), (221, 259, 5), (260, float('inf'), 0)
        ],
        "creatinine": [
            (0, 0.59, 5), (0.6, 1.3, 10), (1.31, 1.5, 5), (1.6, float('inf'), 0)
        ] if gender == "male" else [
            (0, 0.59, 5), (0.6, 1.1, 10), (1.2, 1.5, 5), (1.6, float('inf'), 0)
        ],
        "wbc": [
            (0, 2999, 0), (3000, 3999, 5), (4000, 11000, 10), (11001, float('inf'), 5)
        ]
    }

def get_step_ranges(age):
    """
    Returns step count score ranges based on age.
    """
    return {
        "steps": [
            (0, 4999, 0), (5000, 7499, 5), (7500, 9999, 10), (10000, float('inf'), 15)
        ] if age <= 30 else [
            (0, 4999, 0), (5000, 7499, 5), (7500, 8999, 10), (9000, float('inf'), 15)
        ] if age <= 50 else [
            (0, 2999, 0), (3000, 4999, 5), (5000, 7499, 10), (7500, float('inf'), 15)
        ] if age <= 65 else [
            (0, 1999, 0), (2000, 4999, 5), (5000, 6499, 10), (6500, float('inf'), 15)
        ]
    }

def get_sleep_ranges(age):
    """
    Returns sleep duration score ranges based on age.
    """
    return {
        "sleep": [
            (0, 4.9, 0), (5, 6.9, 5), (7, 9, 10)
        ] if age <= 25 else [
            (0, 4.9, 0), (5, 6.9, 5), (7, 9, 10)
        ] if age <= 40 else [
            (0, 4.4, 0), (4.5, 6.9, 5), (7, 9, 10)
        ] if age <= 60 else [
            (0, 3.9, 0), (4, 6.9, 5), (7, 8.5, 10)
        ]
    }
