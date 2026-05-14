import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()

client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def generate_flashcards(text, num_cards=10):
    prompt = f"""You are a study assistant. Given the following text, generate {num_cards} flashcards.

Return ONLY a JSON array with no extra text or markdown. Each object must have exactly two keys: "question" and "answer".

Example format:
[{{"question": "What is X?", "answer": "X is..."}}]

Text:
{text[:4000]}"""

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = response.content[0].text.strip()
    raw = raw.replace("```json", "").replace("```", "").strip()

    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        print("Raw response:", raw)
        return []