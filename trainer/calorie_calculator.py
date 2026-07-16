"""
calorie_calculator.py
---------------------
Calculates calories burned during workouts.
"""

from trainer.exercises import get_exercise


def calculate_calories(
    exercise_name,
    weight,
    duration_minutes
):
    """
    Calories Burned =
    MET × Weight(kg) × Duration(hours)
    """

    exercise = get_exercise(exercise_name)

    if exercise is None:
        return 0

    duration_hours = duration_minutes / 60

    calories = (
        exercise.met *
        weight *
        duration_hours
    )

    return round(calories, 2)