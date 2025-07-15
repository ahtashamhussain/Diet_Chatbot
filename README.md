# 🥗 AI-Powered Diet Chatbot

This is a smart, AI-powered chatbot that provides personalized diet plans and health suggestions based on user input like age, weight, goals, activity level, and medical conditions.

Built with **FastAPI**, **OpenAI GPT**, and deployed with **Render / Streamlit**.

---

## 🚀 Features

- ✅ Personalized meal plans using GPT
- ✅ Custom inputs: age, weight, height, goals, etc.
- ✅ Built with FastAPI (backend)
- ✅ Frontend using Streamlit (optional)
- ✅ Free deployment-ready

---

## 🛠️ How to Run Locally

```bash
# 1. Clone this repo
git clone https://github.com/ahtashamhussain/Diet_Chatbot.git

# 2. Navigate into the folder
cd Diet_Chatbot

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set your OpenAI API key in a `.env` file
echo "OPENAI_API_KEY=your-key-here" > .env

# 5. Start the server
uvicorn main:app --reload
