"""
insights.py
-----------
Generates AI insights from workout history.
"""

from database.workout_db import (
    get_total_workouts,
    get_total_calories,
    get_total_reps
)


def generate_insights():

    total_workouts = get_total_workouts()
    total_calories = get_total_calories()
    total_reps = get_total_reps()

    insights = []

    if total_workouts == 0:

        insights.append(
            "You haven't completed any workouts yet. Let's start today!"
        )

    else:

        insights.append(
            f"You have completed {total_workouts} workouts."
        )

        insights.append(
            f"You have burned {round(total_calories,1)} calories."
        )

        insights.append(
            f"You have completed {total_reps} total repetitions."
        )

        if total_workouts >= 10:

            insights.append(
                "Excellent consistency! Keep it up."
            )

        elif total_workouts >= 5:

            insights.append(
                "You're building a healthy routine."
            )

        else:

            insights.append(
                "Keep exercising regularly to build momentum."
            )

    return insights