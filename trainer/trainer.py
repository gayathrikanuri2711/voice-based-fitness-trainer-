"""
trainer.py
-----------
Voice-guided trainer for different workout modes.
"""

import time

# Time delay (seconds) between rep counts
SPEEDS = {
    "Slow": 2.0,
    "Medium": 1.2,
    "Fast": 0.8
}


class VoiceTrainer:

    def __init__(self):
        pass

    def countdown(self):
        """Countdown before starting."""
        print("Get Ready!")

        for i in [3, 2, 1]:
            print(i)
            time.sleep(1)

        print("Start!\n")

    def rep_workout(self, reps, speed):
        """Rep-based workout."""

        delay = SPEEDS.get(speed, 1.2)

        self.countdown()

        for rep in range(1, reps + 1):

            print(f"Rep {rep}")

            if rep == reps // 2:
                print("Halfway there!")

            if reps - rep == 5:
                print("Only 5 reps remaining!")

            time.sleep(delay)

        print("\nWorkout Completed!")

    def timer_workout(self, duration):
        """Timer-based workout."""

        self.countdown()

        for sec in range(duration, 0, -1):

            mins = sec // 60
            secs = sec % 60

            print(f"{mins:02}:{secs:02}")

            if sec == 30:
                print("30 seconds remaining!")

            if sec == 10:
                print("10 seconds remaining!")

            time.sleep(1)

        print("\nWorkout Completed!")

    def surya_namaskar(self, rounds):
        """Basic Surya Namaskar rounds."""

        self.countdown()

        for r in range(1, rounds + 1):

            print(f"\nRound {r}")

            print("Pranamasana")
            time.sleep(2)

            print("Hasta Uttanasana")
            time.sleep(2)

            print("Padahastasana")
            time.sleep(2)

            print("Ashwa Sanchalanasana")
            time.sleep(2)

            print("Dandasana")
            time.sleep(2)

            print("Ashtanga Namaskara")
            time.sleep(2)

            print("Bhujangasana")
            time.sleep(2)

            print("Parvatasana")
            time.sleep(2)

            print("Ashwa Sanchalanasana")
            time.sleep(2)

            print("Padahastasana")
            time.sleep(2)

            print("Hasta Uttanasana")
            time.sleep(2)

            print("Pranamasana")
            time.sleep(2)

        print("\nSurya Namaskar Completed!")