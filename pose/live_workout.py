import streamlit as st

st.set_page_config(
    page_title="Live Workout",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 Live AI Workout")

st.info("Live workout module is under development.")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📷 Camera Feed")
    st.empty()

with col2:

    st.subheader("Workout Stats")

    st.metric("Reps", "0")
    st.metric("Calories", "0 kcal")
    st.metric("Time", "00:00")
    st.metric("Stage", "UP")

st.button("▶ Start Live Workout")