from flask import Blueprint, request, jsonify
from app.llm.prompt_builder import build_prompt
from app.llm.ollama_handler import call_ollama

api = Blueprint('api', __name__)

@api.route('/translate', methods=['POST'])
def translate():
    data = request.json
    text = data.get('text')
    target_lang = data.get('target_lang')
    style = data.get('style', None)
    tone_preserve = data.get('tone_preserve', False)
    poetic = data.get('poetic', False)
    model = data.get('model', 'llama3:8b')  # default to llama3:8b

    prompt = build_prompt(text, target_lang, style, tone_preserve, poetic)
    output = call_ollama(prompt, model)

    return jsonify({"output": output})
