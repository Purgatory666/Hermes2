import requests

# Test the complete frontend-to-backend integration with all new UI features

def test_ui_integration():
    """Test the complete frontend-to-backend integration with all UI features."""
    url = "http://localhost:5001/translate"
    
    # Test data that simulates what the frontend would send via AJAX
    test_cases = [
        {
            'name': 'Basic translation',
            'data': {
                'text': 'Hello, how are you today?',
                'target_lang': 'Spanish',
                'model': 'llama3:8b'
            }
        },
        {
            'name': 'Translation with style',
            'data': {
                'text': 'Hello, how are you today?',
                'target_lang': 'Spanish',
                'style': 'formal',
                'model': 'llama3:8b'
            }
        },
        {
            'name': 'Translation with poetic style',
            'data': {
                'text': 'The sun sets behind the mountains, painting the sky in hues of orange and pink.',
                'target_lang': 'French',
                'style': 'poetic',
                'model': 'llama3:8b'
            }
        }
    ]
    
    # Headers to simulate AJAX request
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    for test_case in test_cases:
        print(f"\nTesting: {test_case['name']}")
        try:
            # This simulates the frontend AJAX request
            response = requests.post(url, data=test_case['data'], headers=headers)
            print(f"Status Code: {response.status_code}")
            
            if response.status_code == 200:
                json_response = response.json()
                print(f"Success: Translation received")
                print(f"Translation: {json_response['output'][:100]}...")
            else:
                print(f"Error response: {response.text}")
                
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_ui_integration()
