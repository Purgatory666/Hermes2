from flask import Blueprint, request, jsonify
from app.llm.prompt_builder import build_prompt
from app.llm.ollama_handler import call_ollama

api = Blueprint('api', __name__)

@api.route('/translate', methods=['POST'])
def translate():
    """API endpoint for translating text using Ollama.
    
    Request Body:
        text (str, required): The text to translate
        target_lang (str, required): Target language for translation
        writing_style (str, optional): Writing style/genre for output
        originality (bool, optional): Whether to preserve original aspects (default: false)
        dialect (str, optional): Specific dialect to use
        creative_intent (str, optional): Additional creative instructions
        model (str, optional): Ollama model to use (default: "llama3:8b")
    
    Returns:
        JSON: {"output": "Translated text"}
    """
    # Validate request data
    if not request.is_json:
        return jsonify({'error': 'Request must be JSON'}), 400
    
    data = request.get_json()
    
    # Required parameters
    text = data.get('text')
    target_lang = data.get('target_lang', 'English')
    
    # Validate required parameters
    if not text:
        return jsonify({'error': 'Missing required parameter: text'}), 400
    
    if not target_lang:
        return jsonify({'error': 'Missing required parameter: target_lang'}), 400
    
    # Optional parameters with defaults
    writing_style = data.get('writing_style')
    originality = data.get('originality', False)
    dialect = data.get('dialect')
    creative_intent = data.get('creative_intent')
    model = data.get('model', 'llama3:8b')
    
    # Build prompt and call Ollama (translate mode is default)
    prompt = build_prompt(text, target_lang, writing_style, originality, dialect, creative_intent)
    output = call_ollama(prompt, model)
    
    return jsonify({'output': output})
