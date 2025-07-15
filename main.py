from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
client = OpenAI()

app = FastAPI()

class UserProfile(BaseModel):
    name: str
    age: int
    gender: str
    weight: float
    height: float
    goal: str
    activity: str
    diet: str
    conditions: str = "None"

def create_prompt(data: UserProfile):
    return f"""
You are a certified dietitian. Give a personalized diet plan for:
Name: {data.name}
Age: {data.age}
Gender: {data.gender}
Weight: {data.weight}
Height: {data.height}
Goal: {data.goal}
Activity: {data.activity}
Diet: {data.diet}
Medical Conditions: {data.conditions}
Return detailed diet plan and health advice.
"""

@app.post("/health-plan")
def get_plan(profile: UserProfile):
    prompt = create_prompt(profile)
    chat_completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a health expert."},
            {"role": "user", "content": prompt}
        ]
    )
    return {"plan": chat_completion.choices[0].message.content}
