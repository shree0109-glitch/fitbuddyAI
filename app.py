import streamlit as st
from google import genai
import time

st.title("💪 FitBuddy AI")
st.write("AI Workout Plan Generator")

# Gemini API connection
client = genai.Client(
    api_key=st.secrets["GEMINI_API_KEY"]
)

# Choose goal
goal = st.selectbox(
    "Choose your goal",
    ["Muscle Gain", "Weight Loss", "Fitness"]
)

# Choose intensity
intensity = st.selectbox(
    "Choose intensity",
    ["Low", "Medium", "High"]
)

# Generate workout plan
if st.button("Generate Workout Plan"):

    prompt = f"""
    Create a 7-day workout plan for {goal}
    with {intensity} intensity.

    Include warm-up exercises,
    sets, reps, cooldown and rest days.

    Keep the plan simple and easy to understand.
    """

    # Try Gemini up to 3 times if server is temporarily busy
    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model="gemini-3.8-flash",
                contents=prompt
            )

            st.subheader("🏋️ Your Workout Plan")
            st.write(response.text)

            break

        except Exception as e:

            if "503" in str(e) or "UNAVAILABLE" in str(e):

                if attempt < 2:
                    time.sleep(5)
                else:
                    st.error(
                        "Gemini is temporarily busy. "
                        "Please wait a few minutes and try again."
                    )

            else:
                st.error("Something went wrong.")
                st.exception(e)
                break
