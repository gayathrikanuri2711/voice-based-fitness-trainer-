"""
motivation.py
-------------
Contains motivational messages for the AI Coach.
"""

import random


START_MESSAGES = [

    "Welcome back! Let's make today count.",

    "Ready to crush your workout?",

    "Every workout brings you closer to your goal.",

    "Let's begin. Stay focused and stay strong.",

    "Today is another opportunity to improve."
]


HALFWAY_MESSAGES = [

    "Excellent! You're halfway there.",

    "Keep going. You're doing great.",

    "Half the workout is complete.",

    "Stay strong. You're making progress."
]


FINAL_MESSAGES = [

    "Only five repetitions remaining.",

    "Final push. You've got this!",

    "Almost there. Finish strong!"
]


TIMER_30 = [

    "Thirty seconds remaining.",

    "Only thirty seconds left."
]


TIMER_10 = [

    "Ten seconds remaining.",

    "Final ten seconds.",

    "Don't stop now!"
]


COMPLETION_MESSAGES = [

    "Fantastic work! Workout completed.",

    "Excellent session today.",

    "You should be proud of yourself.",

    "Another workout successfully completed.",

    "Great consistency. Keep it up!"
]


DAILY_MOTIVATION = [

    "Discipline beats motivation.",

    "Small improvements lead to big results.",

    "Success is built one workout at a time.",

    "Stay consistent.",

    "Progress is progress, no matter how small.",

    "You are stronger than yesterday.",

    "Your future self will thank you.",

    "Believe in yourself."
]


def random_start():
    return random.choice(START_MESSAGES)


def random_halfway():
    return random.choice(HALFWAY_MESSAGES)


def random_final():
    return random.choice(FINAL_MESSAGES)


def random_timer30():
    return random.choice(TIMER_30)


def random_timer10():
    return random.choice(TIMER_10)


def random_completion():
    return random.choice(COMPLETION_MESSAGES)


def daily_motivation():
    return random.choice(DAILY_MOTIVATION)