from trainer.exercises import (
    exercise_exists,
    get_mode,
    get_exercise
)

print(exercise_exists("Pushups"))
print(get_mode("Plank"))
print(get_mode("Surya Namaskar"))

exercise = get_exercise("Squats")

print(exercise)
print(exercise.display_name)
print(exercise.met)