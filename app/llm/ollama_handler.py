import requests

def call_ollama(prompt, model="llama3:8b"):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            }
        )
        result = response.json()
        return result.get("response", "No response from model.")
    except Exception as e:
        return f"Error contacting Ollama: {str(e)}"
