"""
timer.py
---------
Workout countdown timer.
"""

import time


class WorkoutTimer:

    def __init__(self, duration):
        """
        duration -> seconds
        """
        self.duration = duration
        self.remaining = duration
        self.running = False
        self.paused = False

    def start(self):
        """
        Start countdown timer.
        """
        self.running = True

        while self.remaining > 0 and self.running:

            if self.paused:
                time.sleep(0.5)
                continue

            mins = self.remaining // 60
            secs = self.remaining % 60

            print(f"{mins:02}:{secs:02}")

            time.sleep(1)

            self.remaining -= 1

        if self.remaining == 0:
            print("\nWorkout Complete!")

    def pause(self):
        self.paused = True

    def resume(self):
        self.paused = False

    def stop(self):
        self.running = False

    def reset(self):
        self.remaining = self.duration
        self.running = False
        self.paused = False