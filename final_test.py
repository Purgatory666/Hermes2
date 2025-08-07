import requests

# Test the complete frontend-to-backend integration with AJAX-style request

def test_ajax_integration():
    """Test the AJAX-style frontend-to-backend integration."""
    url = "http://localhost:5001/translate"
    
    # Test data that simulates what the frontend would send via AJAX
    data = {
        'text': 'Hello, how are you today?',
        'target_lang': 'Spanish',
        'style': 'formal',
        'tone_preserve': 'on',
        'model': 'llama3:8b'
    }
    
    # Headers to simulate AJAX request
    headers = {
        'X-Requested-With': 'XMLHttpRequest'
    }
    
    try:
        # This simulates the frontend AJAX request
        response = requests.post(url, data=data, headers=headers)
        print(f"Status Code: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        
        if response.status_code == 200:
            json_response = response.json()
            print(f"Response JSON: {json_response}")
            print(f"Contains output: {'output' in json_response}")
            if 'output' in json_response:
                print(f"Translation: {json_response['output'][:100]}...")
        else:
            print(f"Error response: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_ajax_integration()
