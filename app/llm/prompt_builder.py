def build_prompt(text, target_lang, style=None, tone_preserve=False, poetic=False):
    prompt = f"Translate the following into {target_lang}."

    if tone_preserve:
        prompt += " Preserve the original tone and writing style."
    if style:
        prompt += f" Use a {style} style."
    if poetic:
        prompt += " Make it poetic or lyrical."

    prompt += f"\n\nInput:\n{text}\n\nOutput:"
    return prompt
