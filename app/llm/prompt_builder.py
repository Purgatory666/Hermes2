def build_prompt(text, target_lang='English', writing_style=None, originality=False, 
                 dialect=None, creative_intent=None):
    """Build a prompt for the translation task based on the provided parameters.
    
    Args:
        text (str): The text to translate
        target_lang (str): Target language for translation
        writing_style (str, optional): Writing style/genre for output
        originality (bool): Whether to preserve original aspects (meaning, tone, voice, format)
        dialect (str, optional): Specific dialect to use
        creative_intent (str, optional): Additional creative instructions
        
    Returns:
        str: The constructed prompt
    """
    
    # Base instruction for translation
    prompt = f"Translate the following text into {target_lang}. Return ONLY the translation without any additional text, explanations, or notes."
    
    # Handle originality preservation
    if originality:
        prompt += " Preserve the original meaning, tone, voice/personality, and format (poem or prose)."
    
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
