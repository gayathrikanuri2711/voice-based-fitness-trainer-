from trainer.workout_manager import WorkoutManager

manager = WorkoutManager()

manager.start_workout(
    "pushups",
    target_reps=20
)

manager.add_rep()
manager.add_rep()
manager.add_rep()

manager.update_calories(5.8)

print(manager.get_summary())

manager.pause_workout()

print(manager.get_summary())

manager.resume_workout()

manager.stop_workout()

print(manager.get_summary())