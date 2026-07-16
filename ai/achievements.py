"""
achievements.py
---------------
Achievement system for AI Fitness Trainer.
"""

from database.workout_db import (
    get_total_workouts,
    get_total_reps,
    get_total_calories
)


def unlocked_achievements():

    achievements = []

    workouts = get_total_workouts()
    reps = get_total_reps()
    calories = get_total_calories()

    if workouts >= 1:
        achievements.append("🥇 First Workout")

    if workouts >= 10:
        achievements.append("🏆 Workout Warrior")

    if workouts >= 50:
        achievements.append("💪 Fitness Legend")

    if reps >= 100:
        achievements.append("💯 100 Reps Club")

    if reps >= 1000:
        achievements.append("🔥 1000 Reps Club")

    if calories >= 500:
        achievements.append("🔥 Burned 500 Calories")

    if calories >= 5000:
        achievements.append("🚀 Burned 5000 Calories")

    return achievements