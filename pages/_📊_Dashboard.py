import streamlit as st
import pandas as pd
from ai.recommendation import get_recommendation
from ai.achievements import unlocked_achievements
from ai.insights import generate_insights
from database.analytics import (
    workouts_per_exercise,
    calories_over_time,
    reps_over_time
)

from database.workout_db import (
    get_total_workouts,
    get_total_reps,
    get_total_calories,
    get_total_duration,
    get_latest_workouts,
    get_calorie_history,
    get_exercise_distribution
)
st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AI Fitness Dashboard")

st.markdown("---")

total_workouts = get_total_workouts()
total_reps = get_total_reps()
total_calories = get_total_calories()
total_duration = get_total_duration()

hours = total_duration // 3600
minutes = (total_duration % 3600) // 60

col1, col2, col3, col4 = st.columns(4)

col1.metric("🏋️ Workouts", total_workouts)
col2.metric("🔥 Calories", total_calories)
col3.metric("💪 Reps", total_reps)
col4.metric("⏱ Time", f"{hours}h {minutes}m")

st.markdown("---")

st.subheader("Recent Workouts")

history = get_latest_workouts()

if history:

    st.dataframe(
        history,
        use_container_width=True
    )

else:

    st.info("No workouts yet.")

st.markdown("---")

st.subheader("📈 Calories Burned Over Time")

calories = get_calorie_history()

if calories:

    df = pd.DataFrame(
        calories,
        columns=["Date", "Calories"]
    )

    st.line_chart(
        df.set_index("Date")
    )

st.markdown("---")

st.subheader("🏋️ Exercise Distribution")

exercise_data = get_exercise_distribution()

if exercise_data:

    df = pd.DataFrame(
        exercise_data,
        columns=["Exercise", "Count"]
    )

    st.bar_chart(
        df.set_index("Exercise")
    )

st.markdown("---")
st.subheader("🤖 Today's Workout Recommendation")

goal = "Weight Loss"   # We'll later replace this with the user's profile

recommendations = get_recommendation(goal)

for exercise in recommendations:
    st.success(
        f"{exercise.display_name} ({exercise.mode.upper()})"
    )


st.markdown("---")
st.subheader("🤖 AI Insights")

for insight in generate_insights():
    st.info(insight)



st.markdown("---")
st.subheader("🏆 Achievements")

achievements = unlocked_achievements()

if achievements:
    for achievement in achievements:
        st.success(achievement)
else:
    st.info("No achievements unlocked yet.")



st.markdown("---")
st.subheader("📊 Workout Distribution")

data = workouts_per_exercise()

if data:

    df = pd.DataFrame(
        data,
        columns=["Exercise", "Count"]
    )

    st.bar_chart(
        df.set_index("Exercise")
    )

else:

    st.info("No workout history yet.")

st.markdown("---")
st.subheader("🔥 Calories Burned")

data = calories_over_time()

if data:

    df = pd.DataFrame(
        data,
        columns=["Date", "Calories"]
    )

    st.line_chart(
        df.set_index("Date")
    )

st.markdown("---")
st.subheader("💪 Repetitions")

data = reps_over_time()

if data:

    df = pd.DataFrame(
        data,
        columns=["Date", "Reps"]
    )

    st.line_chart(
        df.set_index("Date")
    )