
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

<img width="1909" height="1032" alt="noFoodWaste_api_test_kannada_1" src="https://github.com/user-attachments/assets/78de4311-2a92-4e36-848b-346d3239adb2" />
<img width="1895" height="983" alt="noFoodWaste_api_test_Hindi_1" src="https://github.com/user-attachments/assets/4a216a43-e4b0-4ab1-bddf-3a801eee178f" />
<img width="1866" height="981" alt="noFoodWaste_api_test_Tamil_1" src="https://github.com/user-attachments/assets/5ae588c0-96f4-45c1-998a-c1fb1550f3ec" />
<img width="1836" height="861" alt="noFoodWaste_api_test_Telugu_1" src="https://github.com/user-attachments/assets/258d9f57-89c0-42b2-a6f8-3e29e4db00ca" />




