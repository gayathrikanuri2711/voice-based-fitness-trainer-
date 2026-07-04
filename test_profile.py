from profile.user_profile import UserProfile

from profile.bmi import (
    calculate_bmi,
    bmi_category
)

from profile.bmr import calculate_bmr

from profile.health_metrics import (
    calculate_tdee,
    water_intake,
    protein_requirement,
    ideal_weight_range
)

user = UserProfile(
    name="Gayathri",
    age=20,
    gender="Female",
    height=165,
    weight=60,
    goal="Fitness",
    activity_level="Moderate"
)

bmi = calculate_bmi(
    user.weight,
    user.height
)

print("=" * 40)

print("User :", user.name)

print("BMI :", bmi)

print("Category :", bmi_category(bmi))

print("BMR :", round(calculate_bmr(user), 2))

print("TDEE :", calculate_tdee(user))

print("Water :", water_intake(user), "L/day")

print(
    "Protein :",
    protein_requirement(user),
    "g/day"
)

print(
    "Ideal Weight :",
    ideal_weight_range(user),
    "kg"
)

print("=" * 40)