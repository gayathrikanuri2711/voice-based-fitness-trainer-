"""
session.py
-----------
Stores the current workout session.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class WorkoutSession:
    exercise: str
    mode: str

    target_reps: int = 0
    completed_reps: int = 0

    target_time: int = 0      # seconds
    elapsed_time: int = 0     # seconds

    calories: float = 0.0

    status: str = "Not Started"

    start_time: datetime = field(default_factory=datetime.now)
    end_time: datetime | None = None

    def start(self):
        """Start the workout."""
        self.status = "Running"
        self.start_time = datetime.now()

    def pause(self):
        """Pause the workout."""
        self.status = "Paused"

    def resume(self):
        """Resume the workout."""
        self.status = "Running"

    def stop(self):
        """Stop the workout."""
        self.status = "Completed"
        self.end_time = datetime.now()

    def add_rep(self):
        """Increase completed reps by one."""
        self.completed_reps += 1

    def update_time(self, seconds: int):
        """Update elapsed workout time."""
        self.elapsed_time += seconds

    def update_calories(self, calories: float):
        """Update calories burned."""
        self.calories = calories

    def remaining_reps(self):
        """Return remaining reps."""
        return max(0, self.target_reps - self.completed_reps)

    def remaining_time(self):
        """Return remaining time."""
        return max(0, self.target_time - self.elapsed_time)

    def summary(self):
        """Return workout summary."""
        return {
            "Exercise": self.exercise,
            "Mode": self.mode,
            "Completed Reps": self.completed_reps,
            "Remaining Reps": self.remaining_reps(),
            "Elapsed Time": self.elapsed_time,
            "Calories": round(self.calories, 2),
            "Status": self.status
        }