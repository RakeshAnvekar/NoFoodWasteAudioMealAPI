import json
import re
from openai import OpenAI
from app.config import OPENAI_API_KEY
from app.models import FoodMetadata

client = OpenAI(api_key=OPENAI_API_KEY)

def extract_metadata(transcript: str) -> FoodMetadata:

    prompt = f"""
Extract food donation details from the transcript.

IMPORTANT:
- Return all values strictly in English.
- If a field is missing, return null.
- Return JSON only.

Fields:
location, food_items, quantity, quality, pickup_time

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "Return structured JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    content = response.choices[0].message.content

    json_match = re.search(r"\{.*\}", content, re.DOTALL)
    if not json_match:
        raise ValueError("Invalid JSON from LLM")

    data = json.loads(json_match.group())

    #  Normalize food_items
    if not data.get("food_items"):
        data["food_items"] = None
    elif isinstance(data["food_items"], str):
        data["food_items"] = [data["food_items"]]

    #  Normalize quantity
    if isinstance(data.get("quantity"), (int, float)):
        data["quantity"] = str(data["quantity"])

    #  Ensure missing fields exist
    data.setdefault("location", None)
    data.setdefault("quantity", None)
    data.setdefault("quality", None)
    data.setdefault("pickup_time", None)

    return FoodMetadata(**data)
