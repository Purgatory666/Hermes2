def build_prompt(text, target_lang='English', writing_style=None, originality=None, 
                 dialect=None, creative_intent=None):
    """Build a prompt for the translation task based on the provided parameters.
    
    Args:
        text (str): The text to translate
        target_lang (str): Target language for translation
        writing_style (str, optional): Writing style/genre for output
        originality (list): List of originality aspects to preserve (meaning, tone, style, voice, form)
        dialect (str, optional): Specific dialect to use
        creative_intent (str, optional): Additional creative instructions
        
    Returns:
        str: The constructed prompt
    """
    
    # Handle originality preservation and rephrasing
    import json
    if originality:
        # Parse JSON string if needed
        if isinstance(originality, str):
            try:
                originality = json.loads(originality)
            except json.JSONDecodeError:
                originality = []
        
        if isinstance(originality, list) and len(originality) > 0:
            # For rephrasing, we'll create a completely different prompt
            rephrasing_instructions = []
            if 'meaning' in originality:
                rephrasing_instructions.append('meaning')
            if 'tone' in originality:
                rephrasing_instructions.append('tone')
            if 'style' in originality:
                rephrasing_instructions.append('style of content')
            if 'voice' in originality:
                rephrasing_instructions.append('original voice/personality')
            if 'form' in originality:
                rephrasing_instructions.append('format (poem or prose)')
            
            if rephrasing_instructions:
                aspects_str = ', '.join(rephrasing_instructions)
                prompt = f"Rephrase the following text in {target_lang} while preserving the original {aspects_str}. CRITICAL INSTRUCTIONS: Return ONLY the rephrased text without any additional text, explanations, commentary, notes, prefixes, suffixes, or formatting. Output only the rephrased text and nothing else."
                
                # Handle writing style
                if writing_style:
                    prompt += f" Use a {writing_style} writing style or genre."
                
                # Handle dialect
                if dialect:
                    prompt += f" Use the {dialect} dialect."
                
                # Handle creative intent
                if creative_intent:
                    prompt += f" {creative_intent}"
                
                # Add the input text
                prompt += f"\n\nInput:\n{text}\n\nOutput:"
                return prompt
    
    # Base instruction for translation with strict output control (when no originality options are selected)
    prompt = f"Translate the following text into {target_lang}. CRITICAL INSTRUCTIONS: Return ONLY the exact translation without any additional text, explanations, commentary, notes, prefixes, suffixes, or formatting. Do not be influenced by the content, tone, or style of the input. Focus solely on providing an accurate translation. Output only the translated text and nothing else."
    
    # Handle writing style
    if writing_style:
        prompt += f" Use a {writing_style} writing style or genre."
    
    # Handle dialect
    if dialect:
        prompt += f" Use the {dialect} dialect."
    
    # Handle creative intent
    if creative_intent:
        prompt += f" {creative_intent}"
    
    # Add the input text
    prompt += f"\n\nInput:\n{text}\n\nOutput:"
    return prompt
