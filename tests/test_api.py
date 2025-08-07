import requests
import json

def test_api_endpoint():
    """Test the translation API endpoint."""
    url = "http://localhost:5001/api/translate"
    
    # Test case 1: Basic translation
    print("Test 1: Basic translation")
    data = {
        "text": "Good morning!",
        "target_lang": "French"
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test case 2: Formal style with tone preservation
    print("Test 2: Formal style with tone preservation")
    data = {
        "text": "Hey buddy, what is up?",
        "target_lang": "German",
        "style": "formal",
        "tone_preserve": True
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test case 3: Poetic translation
    print("Test 3: Poetic translation")
    data = {
        "text": "The sun rises in the east",
        "target_lang": "Italian",
        "poetic": True
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_api_endpoint()
