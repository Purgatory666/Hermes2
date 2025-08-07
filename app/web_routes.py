from flask import Blueprint, request, jsonify, render_template, current_app
from app.llm.prompt_builder import build_prompt
from app.llm.ollama_handler import call_ollama

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/translate', methods=['POST'])
def translate():
    # Get form data
    text = request.form.get('text')
    target_lang = request.form.get('target_lang', 'English')
    style = request.form.get('style')
    tone_preserve = request.form.get('tone_preserve') == 'on'
    poetic = request.form.get('poetic') == 'on'
    model = request.form.get('model', 'llama3:8b')
    
    # Validate input
    if not text:
        return render_template('index.html', error='Please enter text to translate')
    
    # Build prompt and call Ollama
    prompt = build_prompt(text, target_lang, style, tone_preserve, poetic)
    output = call_ollama(prompt, model)
    
    # Render template with result
    return render_template('index.html', result=output, original_text=text, 
                         target_lang=target_lang, style=style, 
                         tone_preserve=tone_preserve, poetic=poetic)
