"""
session.py
-----------
Stores the current workout session.
"""

from dataclasses import dataclass, field
from datetime import datetime

from trainer.exercises import EXERCISES

print("Session file loaded")
print("EXERCISES imported:", len(EXERCISES))

@dataclass
class WorkoutSession:
    exercise: str
    mode: str

    target_reps: int = 0
    completed_reps: int = 0

    target_time: int = 0
    elapsed_time: int = 0

    calories: float = 0.0

    status: str = "Not Started"

    start_time: datetime = field(default_factory=datetime.now)
    end_time: datetime | None = None

    def start(self):
        self.status = "Running"
        self.start_time = datetime.now()

    def pause(self):
        self.status = "Paused"

    def resume(self):
        self.status = "Running"

    def stop(self):
        self.status = "Completed"
        self.end_time = datetime.now()

    def add_rep(self):
        self.completed_reps += 1

    def update_time(self, seconds: int):
        self.elapsed_time += seconds

    def update_calories(self, calories: float):
        self.calories = calories

    def remaining_reps(self):
        return max(0, self.target_reps - self.completed_reps)

    def remaining_time(self):
        return max(0, self.target_time - self.elapsed_time)

    def summary(self):

        exercise_display = self.exercise

        if self.exercise in EXERCISES:
            exercise_display = EXERCISES[self.exercise].display_name

        return {
            "Exercise": exercise_display,
            "Mode": self.mode,
            "Completed Reps": self.completed_reps,
            "Remaining Reps": self.remaining_reps(),
            "Elapsed Time": self.elapsed_time,
            "Calories": round(self.calories, 2),
            "Status": self.status
        }