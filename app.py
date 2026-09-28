import streamlit as st
from google import genai

st.title("💪 FitBuddy AI")
st.write("AI Workout Plan Generator")

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

goal = st.selectbox(
    "Choose your goal",
    ["Muscle Gain", "Weight Loss", "Fitness"]
)

intensity = st.selectbox(
    "Choose intensity",
    ["Low", "Medium", "High"]
)

if st.button("Generate Workout Plan"):

    prompt = f"""
    Create a 7-day workout plan for {goal}
    with {intensity} intensity.

    Include warm-up, exercises,
    sets, reps, cooldown and rest days.
    """

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    st.subheader("🏋️ Your Workout Plan")
    st.write(response.text)
