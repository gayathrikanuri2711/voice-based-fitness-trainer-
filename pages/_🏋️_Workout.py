import streamlit as st

from trainer.exercises import EXERCISES, get_exercise
from trainer.workout_engine import WorkoutEngine
from voice.text_to_speech import TextToSpeech

st.set_page_config(
    page_title="Workout",
    page_icon="🏋️",
    layout="centered"
)

st.title("🏋️ Workout")

engine = WorkoutEngine()
tts = TextToSpeech()

exercise_keys = list(EXERCISES.keys())

selected_key = st.selectbox(
    "Select Exercise",
    exercise_keys,
    format_func=lambda key: EXERCISES[key].display_name
)

exercise = EXERCISES[selected_key]

st.markdown("---")

st.write("### Exercise Details")

st.write(f"**Mode:** {exercise.mode.upper()}")
st.write(f"**Muscle Group:** {exercise.muscle_group}")
st.write(f"**Difficulty:** {exercise.difficulty}")
st.write(f"**MET:** {exercise.met}")

st.markdown("---")

weight = st.number_input(
    "Your Weight (kg)",
    min_value=20,
    max_value=200,
    value=70
)

reps = 0
duration = 0

if exercise.mode == "rep":

    reps = st.number_input(
        "Target Reps",
        min_value=1,
        value=20
    )

elif exercise.mode == "timer":

    duration = st.number_input(
        "Duration (seconds)",
        min_value=10,
        value=60
    )

elif exercise.mode == "yoga":

    reps = st.number_input(
        "Rounds",
        min_value=1,
        value=5
    )

st.markdown("---")

if st.button("▶ Start Workout"):

    tts.speak("Workout Started")

    engine.start(
    selected_key,
    weight,
    reps,
    duration
)

    if exercise.mode == "rep":

        engine.manager.session.completed_reps = reps

    elif exercise.mode == "timer":

        engine.manager.session.elapsed_time = duration

    elif exercise.mode == "yoga":

        engine.manager.session.completed_reps = reps
        engine.manager.session.elapsed_time = reps * 180

    summary = engine.finish()

    tts.speak("Workout Completed")

    st.success("Workout Completed Successfully!")

    st.subheader("Workout Summary")

    st.json(summary)