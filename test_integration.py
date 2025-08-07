import requests

# Test the complete integration by making a request that simulates the frontend

def test_frontend_backend_integration():
    """Test the complete frontend-to-backend integration."""
    url = "http://localhost:5001/translate"
    
    # Test data that simulates what the frontend would send
    data = {
        'text': 'Hello, how are you today?',
        'target_lang': 'Spanish',
        'style': 'formal',
        'tone_preserve': 'on',
        'model': 'llama3:8b'
    }
    
    try:
        # This simulates the frontend form submission
        response = requests.post(url, data=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response contains result: {'result' in response.text}")
        print(f"Response contains error: {'error' in response.text}")
        
        # Print first 500 characters of response to see what we get
        print(f"Response preview: {response.text[:500]}...")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_frontend_backend_integration()
