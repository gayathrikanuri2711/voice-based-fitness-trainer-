import streamlit as st
from streamlit_webrtc import webrtc_streamer

from trainer.workout_engine import WorkoutEngine
from pose.video_processor import VideoProcessor


# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="Live Workout",
    page_icon="🏋️",
    layout="wide"
)

# -------------------------------
# Workout Engine
# -------------------------------

engine = WorkoutEngine()

# -------------------------------
# Exercise Mapping
# -------------------------------

EXERCISE_MAP = {
    "Push-ups": "pushups",
    "Squats": "squats",
    "Lunges": "lunges",
    "Bicep Curls": "bicep curls",
    "Plank": "plank"
}

# -------------------------------
# Sidebar
# -------------------------------

st.sidebar.title("🏋️ Workout Settings")

exercise = st.sidebar.selectbox(
    "Exercise",
    [
        "Push-ups",
        "Squats",
        "Bicep Curls",
        "Lunges",
        "Plank"
    ]
)

mode = st.sidebar.selectbox(
    "Workout Mode",
    [
        "Repetition",
        "Timer"
    ]
)

weight = st.sidebar.number_input(
    "Weight (kg)",
    min_value=20,
    max_value=200,
    value=60
)

if mode == "Repetition":

    target = st.sidebar.number_input(
        "Target Reps",
        min_value=1,
        value=20
    )

else:

    target = st.sidebar.number_input(
        "Target Time (seconds)",
        min_value=10,
        value=60
    )

start = st.sidebar.button("▶ Start Workout")

# -------------------------------
# Start Workout
# -------------------------------

if start:

    exercise_key = EXERCISE_MAP[exercise]

    st.write("UI Exercise:", exercise)
    st.write("Exercise Key:", exercise_key)

    session = engine.start(
        exercise_name=exercise_key,
        weight=weight,
        target_reps=target if mode == "Repetition" else 0,
        target_time=target if mode == "Timer" else 0
    )

    st.success("✅ Workout Started!")

    st.write(session)

# -------------------------------
# Main UI
# -------------------------------

st.title("🏋️ AI Live Workout")

st.info(f"Selected Exercise: {exercise}")

left, right = st.columns([2, 1])

# -------------------------------
# Camera
# -------------------------------

with left:

    st.subheader("📷 Live Camera")

    webrtc_streamer(
        key="live-workout",
        video_processor_factory=VideoProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False,
        },
    )

# -------------------------------
# Stats
# -------------------------------

with right:

    st.subheader("📊 Workout Stats")

    st.metric("💪 Reps", "0")

    st.metric("📐 Angle", "0°")

    st.metric("🔥 Calories", "0.0 kcal")

    st.metric("⏱ Time", "00:00")

    st.metric("🔄 Stage", "UP")

    st.markdown("---")

    st.subheader("🤖 AI Coach")

    st.info("Let's begin today's workout!")