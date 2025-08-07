import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.llm.prompt_builder import build_prompt
from app.llm.ollama_handler import call_ollama

def test_llm_integration():
    """Test the LLM integration with a simple translation."""
    print("Testing LLM integration...")
    
    # Test prompt building
    text = "Hello, how are you today?"
    target_lang = "Spanish"
    style = "formal"
    tone_preserve = True
    poetic = False
    
    prompt = build_prompt(text, target_lang, style, tone_preserve, poetic)
    print("Generated prompt:")
    print(prompt)
    print("\n" + "="*50 + "\n")
    
    # Test Ollama call
    print("Calling Ollama...")
    response = call_ollama(prompt, "llama3:8b")
    print("Ollama response:")
    print(response)
    
    return response

if __name__ == "__main__":
    test_llm_integration()
