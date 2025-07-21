import streamlit as st
import pandas as pd
import random

# Load dataset
@st.cache_data
def load_data():
    return pd.read_csv("cbt_prompts_period_health_dataset.csv")

df = load_data()

# Title & Instructions
st.set_page_config(page_title="Emotion Detection Quiz – CBT Prompt Selector", layout="centered")
st.title("Emotion Detection Quiz – CBT Prompt Selector")
st.write("Answer all questions honestly to get a CBT-based prompt relevant to your current emotional state during your menstrual cycle.")

# Quiz Questions
quiz = [
    {
        "question": "How do you feel when you wake up?",
        "options": {"Energetic": 2, "Tired": -1, "Anxious": -2}
    },
    {
        "question": "What is your current mood?",
        "options": {"Happy": 2, "Okay": 0, "Low": -2}
    },
    {
        "question": "How are you feeling about your body today?",
        "options": {"Confident": 2, "Neutral": 0, "Insecure": -2}
    },
    {
        "question": "Are you feeling stressed or overwhelmed?",
        "options": {"Not at all": 2, "A little": -1, "Very much": -2}
    },
    {
        "question": "Which phase are you currently in?",
        "options": {"Pre-period": "pre-period", "Menstruation": "menstruation", "Post-period": "post-period"}
    }
]

# Step 1–4: Emotion Questions (Scoring based)
user_score = 0
for q in quiz[:-1]:  # Skip last phase question for now
    st.markdown(f"**{q['question']}**")
    st.radio(label="", options=list(q["options"].keys()), key=q["question"])

# Step 5: Cycle Phase Question
phase_question = quiz[-1]
st.markdown(f"**{phase_question['question']}**")
selected_phase = st.radio(label="", options=list(phase_question["options"].keys()), key=phase_question["question"])

# On Button Click
if st.button("Submit Quiz"):
    # Score Calculation
    for q in quiz[:-1]:
        selected_option = st.session_state[q["question"]]
        user_score += q["options"][selected_option]

    # Cycle Phase
    cycle_phase = phase_question["options"][st.session_state[phase_question["question"]]]

    # Emotion Detection
    emotion_mapping = {
        "very_negative": (-10, -5),
        "low_mood": (-4, -1),
        "neutral": (0,),
        "positive": (1, 4),
        "very_positive": (5, 10)
    }

    category_mapping = {
        "very_negative": "stress_relief",
        "low_mood": "mood_reframe",
        "neutral": "neutral_support",
        "positive": "body_acceptance",
        "very_positive": "confidence_boost"
    }

    detected_emotion = "neutral"
    for emotion, score_range in emotion_mapping.items():
        if isinstance(score_range, tuple):
            if score_range[0] <= user_score <= score_range[1]:
                detected_emotion = emotion
                break
        elif user_score in score_range:
            detected_emotion = emotion
            break

    prompt_category = category_mapping[detected_emotion]

    # Get Prompt matching both category and cycle_phase
    def get_prompt(category, phase):
        subset = df[(df["intent"] == category) & (df["cycle_phase"] == phase)]
        if not subset.empty:
            return subset.sample(1).iloc[0]
        else:
            fallback = df[df["intent"] == category]
            if not fallback.empty:
                return fallback.sample(1).iloc[0]
            return {"prompt": "No prompt available.", "intent": category, "theme": "N/A", "cycle_phase": phase}

    prompt_row = get_prompt(prompt_category, cycle_phase)

    # Show result
    st.write("**Detected Emotion:**", detected_emotion)
    st.write("**Prompt Category:**", prompt_category)
    st.write("**Cycle Phase Selected:**", cycle_phase)
    st.write("**Prompt Theme:**", prompt_row["theme"])
    st.markdown("**Suggested CBT Prompt:**")
    st.markdown(f"*{prompt_row['prompt']}*")
