from trainer.trainer import VoiceTrainer

trainer = VoiceTrainer()

print("Rep Workout")
trainer.rep_workout(
    reps=10,
    speed="Medium"
)

print("\nTimer Workout")
trainer.timer_workout(
    duration=10
)

print("\nSurya Namaskar")
trainer.surya_namaskar(
    rounds=2
)