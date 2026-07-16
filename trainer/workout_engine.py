"""
workout_engine.py
-----------------
Main engine that controls a complete workout.
"""

from datetime import datetime

from trainer.workout_manager import WorkoutManager
from trainer.calorie_calculator import calculate_calories
from database.workout_db import save_workout


class WorkoutEngine:

    def __init__(self):
        self.manager = WorkoutManager()

    def start(
        self,
        exercise_name,
        weight,
        target_reps=0,
        target_time=0
    ):
        """
        Starts a workout session.
        """

        session = self.manager.start_workout(
            exercise_name,
            target_reps,
            target_time
        )

        self.weight = weight

        return session

    def finish(self):
        """
        Completes the workout.
        """

        session = self.manager.session

        if session is None:
            return None

        self.manager.stop_workout()

        duration_minutes = session.elapsed_time / 60

        calories = calculate_calories(
            session.exercise,
            self.weight,
            duration_minutes
        )

        session.update_calories(calories)

        save_workout(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            session.exercise,
            session.completed_reps,
            session.elapsed_time,
            calories
        )

        return session.summary()