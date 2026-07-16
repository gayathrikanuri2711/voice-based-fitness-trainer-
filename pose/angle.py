"""
angle.py
---------
Calculates angle between three body landmarks.
"""

import math


def calculate_angle(a, b, c):
    """
    Calculates the angle formed by points:
    a -> b -> c

    b is the joint.
    """

    ax, ay = a
    bx, by = b
    cx, cy = c

    radians = math.atan2(
        cy - by,
        cx - bx
    ) - math.atan2(
        ay - by,
        ax - bx
    )

    angle = abs(
        radians * 180 / math.pi
    )

    if angle > 180:
        angle = 360 - angle

    return angle