import re
import pandas as pd
import tiktoken
import re

tokenizer = tiktoken.encoding_for_model("gpt-4o-mini")

def manual_text_stats(text):
    text = text.replace("\n", "", 1)

    num_chars = len(text)
    words = re.findall(r'\b\w+\b', text)
    num_words = len(words)
    tokens = tokenizer.encode(text.strip())
    num_tokens = len(tokens)
    num_sentences = len(re.split(r'[.!?]+', text)) - 1
    sentence = text

    return {
        "tokens": num_tokens,
        "characters": num_chars,
        "words": num_words,
        "sentences": num_sentences,
        "sentence": sentence
    }

file_path = '../../datasets/ubertext_gec/ubertext.social.filter_rus_gcld+short.text_only.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text_data = file.read()
    text_data = re.split(r'\n{2,}', text_data)

text_stats_manual = [manual_text_stats(example) for example in text_data]
df_stats_manual = pd.DataFrame(text_stats_manual)

numerical_columns = [
    'tokens',
    'characters',
    'words',
    'sentences',
]
print(df_stats_manual.loc[:, numerical_columns].sum(axis=0))

df_stats_manual.to_csv("../../datasets/ubertext_gec/raw_ubertext_social.csv")
