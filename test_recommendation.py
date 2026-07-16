from ai.recommendation import get_recommendation

goal = "Weight Loss"

plan = get_recommendation(goal)

print(f"\nRecommended Workout for {goal}\n")

for exercise in plan:
    print(
        f"{exercise.display_name} | "
        f"{exercise.mode} | "
        f"{exercise.difficulty}"
    )