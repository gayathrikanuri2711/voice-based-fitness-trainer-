"""
user_profile.py
---------------
Stores user information.
"""

from dataclasses import dataclass


@dataclass
class UserProfile:
    name: str
    age: int
    gender: str
    height: float      # cm
    weight: float      # kg
    goal: str          # Weight Loss / Muscle Gain / Fitness
    activity_level: str