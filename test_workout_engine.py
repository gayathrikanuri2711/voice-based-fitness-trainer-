from trainer.workout_engine import WorkoutEngine

engine = WorkoutEngine()

engine.start(
    exercise_name="Pushups",
    weight=70,
    target_reps=20
)

for _ in range(20):
    engine.manager.add_rep()

engine.manager.update_time(600)  # 10 minutes

summary = engine.finish()

print(summary)