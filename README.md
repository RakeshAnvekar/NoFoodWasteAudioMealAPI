
# 🌿 No Food Waste — Backend API

An AI-powered FastAPI microservice that converts spoken audio (in any language) into an English transcript and extracts structured food donation metadata such as location, food items, quantity, quality, and pickup time.

---

## 🚀 Features

- Accepts audio uploads
- Multilingual speech support
- Speech → English translation
- Metadata extraction using AI
- FastAPI REST API
- JSON responses

---

## 🧱 Tech Stack

- FastAPI
- OpenAI APIs
- Pydantic
- Python

---

## 📁 Project Structure

<img width="276" height="288" alt="image" src="https://github.com/user-attachments/assets/af9aad58-7624-4ffa-8a46-8a9adf8e1619" />


---

## ⚙️ Setup

1. Create virtual environment
python -m venv venv
venv\Scripts\activate

2. Install dependencies
pip install fastapi uvicorn openai python-dotenv python-multipart

3. Add .env file
OPENAI_API_KEY=your_key_here

4. Run server
uvicorn app.main:app --reload

---

## 📡 Endpoint

POST /process-audio?mode=api

Returns transcript + metadata.

---

## 🧾 Example Response

{
  "transcript": "There are 25 meal packets available at Indiranagar",
  "metadata": {
    "location": "Indiranagar",
    "food_items": ["rice", "sambar"],
    "quantity": "25 meals",
    "quality": "good",
    "pickup_time": "6 PM"
  }
}
