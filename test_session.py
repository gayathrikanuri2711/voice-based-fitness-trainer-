from trainer.session import WorkoutSession

session = WorkoutSession(
    exercise="Push-ups",
    mode="rep",
    target_reps=20
)

session.start()

session.add_rep()
session.add_rep()
session.add_rep()

session.update_calories(4.5)

print(session.summary())

session.stop()

print("Workout Status:", session.status)