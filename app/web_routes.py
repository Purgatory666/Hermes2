from flask import Blueprint, request, jsonify, render_template, current_app
from app.llm.prompt_builder import build_prompt
from app.llm.ollama_handler import call_ollama

web = Blueprint('web', __name__)

@web.route('/')
def index():
    return render_template('index.html')

@web.route('/translate', methods=['POST'])
def translate():
    # Check if this is an AJAX request
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    
    # Get form data
    text = request.form.get('text')
    target_lang = request.form.get('target_lang', 'English')
    writing_style = request.form.get('writing_style')
    originality = request.form.get('originality') == 'on'
    dialect = request.form.get('dialect')
    creative_intent = request.form.get('creative_intent')
    model = request.form.get('model', 'llama3:8b')
    
    # Validate input
    if not text:
        if is_ajax:
            return jsonify({'error': 'Please enter text to translate'}), 400
        return render_template('index.html', error='Please enter text to translate')
    
    # Build prompt and call Ollama (translate mode is default)
    prompt = build_prompt(text, target_lang, writing_style, originality, dialect, creative_intent)
    output = call_ollama(prompt, model)
    
    # Return JSON for AJAX requests, HTML for regular form submissions
    if is_ajax:
        return jsonify({'output': output})
    
    # Render template with result for regular form submissions
    return render_template('index.html', result=output, original_text=text, 
                         target_lang=target_lang, writing_style=writing_style,
                         originality=originality, dialect=dialect, creative_intent=creative_intent)
