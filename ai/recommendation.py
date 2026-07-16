"""
recommendation.py
-----------------
Smart workout recommendation engine.
"""

from trainer.exercises import EXERCISES


def get_recommendation(goal: str):
    """
    Returns recommended exercises based on user's goal.
    """

    goal = goal.lower()

    if goal == "weight loss":

        return [
            EXERCISES["jumping jacks"],
            EXERCISES["squats"],
            EXERCISES["burpees"],
            EXERCISES["plank"]
        ]

    elif goal == "muscle gain":

        return [
            EXERCISES["pushups"],
            EXERCISES["lunges"],
            EXERCISES["bicep curls"],
            EXERCISES["plank"]
        ]

    else:

        return [
            EXERCISES["pushups"],
            EXERCISES["squats"],
            EXERCISES["stretching"],
            EXERCISES["surya namaskar"]
        ]