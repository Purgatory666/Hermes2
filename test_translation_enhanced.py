import requests
import json

def test_translation(payload, description):
    print(f"\n=== Testing: {description} ===")
    print(f"Request: {payload}")
    
    try:
        response = requests.post(
            "http://127.0.0.1:5000/api/translate",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        print(f"Status Code: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()['output']}")
        else:
            print(f"Error: {response.text}")
    except Exception as e:
        print(f"Error: {str(e)}")

# Test 1: Basic translation
payload1 = {
    "text": "Good morning, how are you?",
    "target_lang": "French"
}
test_translation(payload1, "Basic French translation")

# Test 2: Translation with style
payload2 = {
    "text": "Welcome to our new restaurant!",
    "target_lang": "Japanese",
    "style": "casual"
}
test_translation(payload2, "Japanese translation with casual style")

# Test 3: Translation with tone preservation
payload3 = {
    "text": "I'm so excited about this opportunity!",
    "target_lang": "German",
    "tone_preserve": True
}
test_translation(payload3, "German translation with tone preservation")

# Test 4: Poetic translation
payload4 = {
    "text": "The sunset painted the sky in hues of orange and pink.",
    "target_lang": "Italian",
    "poetic": True
}
test_translation(payload4, "Poetic Italian translation")
