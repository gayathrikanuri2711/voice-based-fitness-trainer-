"""
health_metrics.py
-----------------
Calculates health metrics from user profile.
"""

from profile.bmr import calculate_bmr


ACTIVITY_MULTIPLIERS = {
    "Sedentary": 1.2,
    "Light": 1.375,
    "Moderate": 1.55,
    "Active": 1.725,
    "Very Active": 1.9
}


def calculate_tdee(profile):
    """
    Total Daily Energy Expenditure
    """

    bmr = calculate_bmr(profile)

    multiplier = ACTIVITY_MULTIPLIERS.get(
        profile.activity_level,
        1.2
    )

    return round(bmr * multiplier, 2)


def water_intake(profile):
    """
    Water recommendation (Litres/day)
    """

    litres = profile.weight * 0.035

    return round(litres, 2)


def protein_requirement(profile):
    """
    Protein recommendation (grams/day)
    """

    goal = profile.goal.lower()

    if goal == "weight loss":
        protein = profile.weight * 1.6

    elif goal == "muscle gain":
        protein = profile.weight * 2.0

    else:
        protein = profile.weight * 1.2

    return round(protein, 1)


def ideal_weight_range(profile):
    """
    Returns healthy weight range based on BMI 18.5–24.9
    """

    height = profile.height / 100

    minimum = 18.5 * (height ** 2)
    maximum = 24.9 * (height ** 2)

    return (
        round(minimum, 1),
        round(maximum, 1)
    )