"""
coach.py
---------
Main AI Coach.
"""

from ai import motivation


class AICoach:

    def workout_start(self):
        return motivation.random_start()

    def halfway(self):
        return motivation.random_halfway()

    def final_reps(self):
        return motivation.random_final()

    def timer30(self):
        return motivation.random_timer30()

    def timer10(self):
        return motivation.random_timer10()

    def completed(self):
        return motivation.random_completion()

    def motivation(self):
        return motivation.daily_motivation()