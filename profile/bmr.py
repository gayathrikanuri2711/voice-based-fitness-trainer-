"""
bmr.py
-------
BMR Calculator
"""


def calculate_bmr(profile):

    if profile.gender.lower() == "male":

        return (
            10 * profile.weight +
            6.25 * profile.height -
            5 * profile.age +
            5
        )

    return (
        10 * profile.weight +
        6.25 * profile.height -
        5 * profile.age -
        161
    )