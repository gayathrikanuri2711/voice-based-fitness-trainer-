from datetime import datetime

from database.workout_db import (
    save_workout,
    get_all_workouts,
    get_total_workouts,
    get_total_reps,
    get_total_calories,
    clear_history
)

print("Clearing old history...")
clear_history()

print("Saving workouts...")

save_workout(
    str(datetime.now().date()),
    "Pushups",
    20,
    5,
    45.5
)

save_workout(
    str(datetime.now().date()),
    "Squats",
    30,
    10,
    80.0
)

save_workout(
    str(datetime.now().date()),
    "Plank",
    0,
    3,
    20.5
)

print("\nWorkout History")

for workout in get_all_workouts():
    print(workout)

print("\nStatistics")

print("Total Workouts :", get_total_workouts())

print("Total Reps :", get_total_reps())

print("Total Calories :", get_total_calories())