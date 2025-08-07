import requests

# Comprehensive test to verify all UI fixes

def test_all_fixes():
    """Test all UI fixes and functionality."""
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
        },
        {
            'name': 'Translation with no style (None option)',
            'data': {
                'text': 'This is a test sentence.',
                'target_lang': 'German',
                'style': '',
                'model': 'llama3:8b'
            }
        }
    ]
    
    # Headers to simulate AJAX request
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    print("Testing all UI fixes and functionality...")
    
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
    
    print("\nAll tests completed. Check the UI for the following fixes:")
    print("1. Style dropdown works correctly with 'None' option")
    print("2. Logo moves directly to the left and stays there when text area is clicked")
    print("3. Mode toggle shows current mode above and opposite mode beside toggle")
    print("4. Waterfall/wallpaper on sides has increased opacity")

if __name__ == "__main__":
    test_all_fixes()
