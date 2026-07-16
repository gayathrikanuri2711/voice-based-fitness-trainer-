"""
rep_counter.py
--------------
Generic rep counter using joint angles.
"""


class RepCounter:

    def __init__(self, up_angle=160, down_angle=70):

        self.up_angle = up_angle
        self.down_angle = down_angle

        self.counter = 0
        self.stage = "up"

    def update(self, angle):
        """
        Update rep count based on joint angle.

        Returns:
            reps, stage
        """

        if angle > self.up_angle:
            self.stage = "up"

        if angle < self.down_angle and self.stage == "up":
            self.stage = "down"

        elif angle > self.up_angle and self.stage == "down":
            self.stage = "up"
            self.counter += 1

        return self.counter, self.stage

    def reset(self):

        self.counter = 0
        self.stage = "up"