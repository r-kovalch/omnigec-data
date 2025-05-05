def normalize_spaces(text):
    return ' '.join(text.split())

def generate_original_corrected_texts(original_text, corrected_text):
    # Split the original and corrected texts
    original_words = original_text.split()
    corrected_words = corrected_text.split()

    # Initialize empty lists for marked original and corrected texts
    marked_original_text = []
    marked_corrected_text = []

    # Track words from the original text that were removed
    removed_words = set(original_words) - set(corrected_words)

    # Track words from the corrected text that were added
    added_words = set(corrected_words) - set(original_words)

    # Mark removed words in the original text as red
    for word in original_words:
        if word in removed_words:
            marked_original_text.append('\033[91m\033[1m' + word + '\033[0m')
        else:
            marked_original_text.append(word)

    # Mark added words in the corrected text as green
    for word in corrected_words:
        if word in added_words:
            marked_corrected_text.append('\033[92m\033[1m' + word + '\033[0m')
        else:
            marked_corrected_text.append(word)

    return (' '.join(marked_original_text), ' '.join(marked_corrected_text))

def get_multi_gec_correction_comparison_text(multi_gec_output: dict, original_text: str) -> str:
    multi_gec_correction_comparison_text: str = ""

    for i, correction_reasoning in enumerate(multi_gec_output):
        correction = correction_reasoning["correction"]
        reasoning = correction_reasoning["explanation"]

        text1 = normalize_spaces(original_text)
        text2 = normalize_spaces(correction)

        original_corrected_text = generate_original_corrected_texts(
            original_text=text1,
            corrected_text=text2)

        multi_gec_correction_comparison_text += f"""
    Correction: {i}

    Original Text:
    {original_corrected_text[0]}

    Corrected Text:
    {original_corrected_text[1]}

    Reasoning:
    {reasoning}
        """

    return multi_gec_correction_comparison_text
