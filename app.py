import streamlit as st
import requests

st.title("🥗 AI-Powered Diet Plan Chatbot")

st.markdown("Fill in the details to get a personalized diet plan.")

with st.form("diet_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1, max_value=120)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    weight = st.number_input("Weight (kg)")
    height = st.number_input("Height (cm)")
    goal = st.selectbox("Goal", ["Weight Loss", "Weight Gain", "Maintain Weight"])
    activity = st.selectbox("Activity Level", ["Sedentary", "Moderate", "Active"])
    diet = st.selectbox("Diet Preference", ["Vegetarian", "Non-Vegetarian", "Vegan"])
    conditions = st.text_input("Medical Conditions (if any)", value="None")

    submit = st.form_submit_button("Get Diet Plan")

if submit:
    with st.spinner("Generating diet plan..."):
        url = "http://127.0.0.1:8000/health-plan"
        user_data = {
            "name": name,
            "age": age,
            "gender": gender,
            "weight": weight,
            "height": height,
            "goal": goal,
            "activity": activity,
            "diet": diet,
            "conditions": conditions
        }

        try:
            response = requests.post(url, json=user_data)
            if response.status_code == 200:
                plan = response.json()["plan"]
                st.success("Here's your personalized diet plan:")
                st.markdown(plan)
            else:
                st.error(f"Error: {response.status_code}")
        except Exception as e:
            st.error(f"Could not connect to the backend: {e}")
