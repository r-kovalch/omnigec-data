import nltk
import re

def average_edit_distance(text1, text2):
    # Split texts into sentences
    sentences1 = re.split(r'[.!?]\s*', text1)
    sentences2 = re.split(r'[.!?]\s*', text2)

    # Remove any empty strings from sentence lists
    sentences1 = [s for s in sentences1 if s]
    sentences2 = [s for s in sentences2 if s]

    # Calculate the total edit distance for corresponding sentences
    total_distance = 0
    count = 0

    # Use zip to iterate over pairs of sentences
    for sent1, sent2 in zip(sentences1, sentences2):
        total_distance += nltk.edit_distance(sent1, sent2)
        count += 1

    # Calculate the average edit distance
    avg_distance = total_distance / count if count > 0 else 0
    return avg_distance