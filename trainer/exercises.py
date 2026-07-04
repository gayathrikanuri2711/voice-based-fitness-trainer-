"""
Exercise Database
-----------------
This module contains all supported exercises and their metadata.

Every exercise has:
- display_name
- mode (rep / timer / yoga)
- muscle_group
- difficulty
- MET value (used for calorie calculation)
"""

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Exercise:
    display_name: str
    mode: str
    muscle_group: str
    difficulty: str
    met: float


EXERCISES: Dict[str, Exercise] = {

    # --------------------------
    # REP BASED EXERCISES
    # --------------------------

    "pushups": Exercise(
        display_name="Push-ups",
        mode="rep",
        muscle_group="Chest",
        difficulty="Medium",
        met=8.0
    ),

    "squats": Exercise(
        display_name="Squats",
        mode="rep",
        muscle_group="Legs",
        difficulty="Easy",
        met=5.0
    ),

    "lunges": Exercise(
        display_name="Lunges",
        mode="rep",
        muscle_group="Legs",
        difficulty="Medium",
        met=6.0
    ),

    "bicep curls": Exercise(
        display_name="Bicep Curls",
        mode="rep",
        muscle_group="Arms",
        difficulty="Easy",
        met=3.5
    ),

    "jumping jacks": Exercise(
        display_name="Jumping Jacks",
        mode="rep",
        muscle_group="Full Body",
        difficulty="Easy",
        met=8.0
    ),

    "burpees": Exercise(
        display_name="Burpees",
        mode="rep",
        muscle_group="Full Body",
        difficulty="Hard",
        met=10.0
    ),

    # --------------------------
    # TIMER BASED EXERCISES
    # --------------------------

    "plank": Exercise(
        display_name="Plank",
        mode="timer",
        muscle_group="Core",
        difficulty="Medium",
        met=3.8
    ),

    "side plank": Exercise(
        display_name="Side Plank",
        mode="timer",
        muscle_group="Core",
        difficulty="Medium",
        met=3.5
    ),

    "wall sit": Exercise(
        display_name="Wall Sit",
        mode="timer",
        muscle_group="Legs",
        difficulty="Medium",
        met=4.5
    ),

    "horse stance": Exercise(
        display_name="Horse Stance",
        mode="timer",
        muscle_group="Legs",
        difficulty="Hard",
        met=5.5
    ),

    "stretching": Exercise(
        display_name="Stretching",
        mode="timer",
        muscle_group="Full Body",
        difficulty="Easy",
        met=2.5
    ),

    # --------------------------
    # YOGA
    # --------------------------

    "surya namaskar": Exercise(
        display_name="Surya Namaskar",
        mode="yoga",
        muscle_group="Full Body",
        difficulty="Medium",
        met=7.0
    ),
}


def get_exercise(name: str) -> Optional[Exercise]:
    """
    Returns Exercise object if found.
    """

    return EXERCISES.get(name.strip().lower())


def exercise_exists(name: str) -> bool:
    """
    Checks whether exercise exists.
    """

    return name.strip().lower() in EXERCISES


def get_mode(name: str) -> Optional[str]:
    """
    Returns:
        rep
        timer
        yoga
    """

    exercise = get_exercise(name)

    if exercise is None:
        return None

    return exercise.mode