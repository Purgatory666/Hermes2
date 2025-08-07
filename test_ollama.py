import requests

# Test the Ollama API directly
def test_ollama():
    prompt = "Translate the following into Spanish. Return ONLY the translation without any additional text, explanations, or notes.\n\nInput:\nHello, how are you?\n\nOutput:"
    
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3:8b",
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        print("Response from Ollama:")
        print(result.get("response", "No response from model."))
    except Exception as e:
        print(f"Error contacting Ollama: {str(e)}")

if __name__ == "__main__":
    test_ollama()
