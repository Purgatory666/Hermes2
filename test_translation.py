import requests
import json

# Test data
payload = {
    "text": "Hello, how are you today?",
    "target_lang": "Spanish",
    "style": "formal",
    "tone_preserve": True,
    "poetic": False,
    "model": "llama3:8b"
}

# Send POST request
try:
    response = requests.post(
        "http://127.0.0.1:5000/api/translate",
        headers={"Content-Type": "application/json"},
        data=json.dumps(payload)
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.json()}")
except Exception as e:
    print(f"Error: {str(e)}")
