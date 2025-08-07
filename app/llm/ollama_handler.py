import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get configuration from environment variables
OLLAMA_BASE_URL = os.getenv('OLLAMA_BASE_URL', 'http://localhost:11434')
DEFAULT_MODEL = os.getenv('DEFAULT_MODEL', 'llama3:8b')

def call_ollama(prompt, model=None):
    """Call the Ollama API to generate a translation.
    
    Args:
        prompt (str): The prompt to send to the model
        model (str, optional): The Ollama model to use
        
    Returns:
        str: The model's response or an error message
    """
    if model is None:
        model = DEFAULT_MODEL
    
    try:
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=120  # 2 minute timeout for translation
        )
        response.raise_for_status()  # Raise an exception for bad status codes
        result = response.json()
        return result.get("response", "No response from model.")
    except requests.exceptions.RequestException as e:
        return f"Error contacting Ollama: {str(e)}"
    except Exception as e:
        return f"Unexpected error: {str(e)}"
