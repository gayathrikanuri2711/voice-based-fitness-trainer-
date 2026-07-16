"""
workout_manager.py
------------------
Controls the workout session.
"""

from trainer.session import WorkoutSession
from trainer.exercises import get_exercise


class WorkoutManager:

    def __init__(self):
        self.session = None

    def start_workout(self, exercise_name, target_reps=0, target_time=0):

        exercise_name = exercise_name.strip().lower()

        exercise = get_exercise(exercise_name)

        if exercise is None:
            raise ValueError("Exercise not found.")

        self.session = WorkoutSession(
            exercise=exercise_name,          # Store the key
            mode=exercise.mode,
            target_reps=target_reps,
            target_time=target_time
    )

        self.session.start()

        return self.session

    def add_rep(self):

        if self.session:
            self.session.add_rep()

    def update_time(self, seconds):

        if self.session:
            self.session.update_time(seconds)

    def update_calories(self, calories):

        if self.session:
            self.session.update_calories(calories)

    def pause_workout(self):

        if self.session:
            self.session.pause()

    def resume_workout(self):

        if self.session:
            self.session.resume()

    def stop_workout(self):

        if self.session:
            self.session.stop()

    def get_summary(self):

        if self.session:
            return self.session.summary()

        return None