# matcher.py

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

def compute_cosine_similarity(resume_text, jd_text):
    resume_clean = clean_text(resume_text)
    jd_clean = clean_text(jd_text)

    vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=5000)
    vectors = vectorizer.fit_transform([resume_clean, jd_clean])
    score = cosine_similarity(vectors[0], vectors[1])[0][0]

    return round(score, 4)

def get_matching_keywords(resume_text, jd_keywords, threshold=75):
    resume_text_lower = re.sub(r'[^a-zA-Z0-9\s]', '', resume_text.lower())
    matched = set()

    for phrase in jd_keywords:
        words = phrase.lower().split()
        for word in words:
            if len(word) < 3:
                continue
            score = fuzz.partial_ratio(word, resume_text_lower)
            if score >= threshold:
                matched.add(phrase)
                break

    return sorted(list(matched))

def compute_combined_score(resume_text, jd_text, jd_keywords):
    cosine_score = compute_cosine_similarity(resume_text, jd_text)
    matched_keywords = get_matching_keywords(resume_text, jd_keywords)
    keyword_coverage = len(matched_keywords) / len(jd_keywords) if jd_keywords else 0

    combined_score = (0.7 * cosine_score) + (0.3 * keyword_coverage)
    return round(combined_score * 100, 2), matched_keywords
