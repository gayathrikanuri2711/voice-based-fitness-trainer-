import streamlit as st

from profile.user_profile import UserProfile
from profile.bmi import calculate_bmi, bmi_category
from profile.bmr import calculate_bmr
from profile.health_metrics import (
    calculate_tdee,
    water_intake,
    protein_requirement,
    ideal_weight_range
)

from database.profile_db import (
    save_user,
    load_user
)

st.title("👤 My Profile")

# -----------------------------
# Load Existing Profile
# -----------------------------

profile = load_user()

if profile is None:

    profile = UserProfile(
        name="",
        age=20,
        gender="Male",
        height=170,
        weight=70,
        goal="Fitness",
        activity_level="Moderate"
    )

# -----------------------------
# User Inputs
# -----------------------------

name = st.text_input(
    "Name",
    value=profile.name
)

age = st.number_input(
    "Age",
    10,
    100,
    profile.age
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"],
    index=0 if profile.gender == "Male" else 1
)

height = st.number_input(
    "Height (cm)",
    100.0,
    250.0,
    float(profile.height)
)

weight = st.number_input(
    "Weight (kg)",
    20.0,
    300.0,
    float(profile.weight)
)

goal = st.selectbox(
    "Fitness Goal",
    [
        "Weight Loss",
        "Muscle Gain",
        "Fitness"
    ],
    index=[
        "Weight Loss",
        "Muscle Gain",
        "Fitness"
    ].index(profile.goal)
)

activity = st.selectbox(
    "Activity Level",
    [
        "Sedentary",
        "Light",
        "Moderate",
        "Active",
        "Very Active"
    ],
    index=[
        "Sedentary",
        "Light",
        "Moderate",
        "Active",
        "Very Active"
    ].index(profile.activity_level)
)

# -----------------------------
# Save Button
# -----------------------------

if st.button("💾 Save Profile"):

    profile = UserProfile(
        name=name,
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        goal=goal,
        activity_level=activity
    )

    save_user(profile)

    st.success("Profile saved successfully!")

# -----------------------------
# Health Metrics
# -----------------------------

profile = UserProfile(
    name=name,
    age=age,
    gender=gender,
    height=height,
    weight=weight,
    goal=goal,
    activity_level=activity
)

bmi = calculate_bmi(profile.weight, profile.height)

st.divider()

st.subheader("📊 Health Metrics")

c1, c2 = st.columns(2)

with c1:

    st.metric("BMI", bmi)

    st.metric(
        "Category",
        bmi_category(bmi)
    )

    st.metric(
        "BMR",
        round(calculate_bmr(profile))
    )

with c2:

    st.metric(
        "TDEE",
        calculate_tdee(profile)
    )

    st.metric(
        "Water Intake",
        f"{water_intake(profile)} L"
    )

    st.metric(
        "Protein",
        f"{protein_requirement(profile)} g"
    )

st.info(
    f"Ideal Weight Range : {ideal_weight_range(profile)} kg"
)