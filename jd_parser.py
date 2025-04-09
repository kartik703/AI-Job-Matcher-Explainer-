# jd_parser.py

from keybert import KeyBERT

kw_model = KeyBERT()

def load_jd_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_keywords_from_jd(text, top_n=10):
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words="english", top_n=top_n)
    return [kw[0] for kw in keywords]
