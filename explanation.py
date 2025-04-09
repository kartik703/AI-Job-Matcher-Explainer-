# explanation.py

from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch

# Load the Flan-T5 model and tokenizer once
tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")

def generate_explanation(jd_keywords, matched_keywords):
    if not jd_keywords or not matched_keywords:
        return "Not enough information to generate an explanation."

    prompt = (
        f"The job requires the following skills: {', '.join(jd_keywords)}. "
        f"The resume includes: {', '.join(matched_keywords)}. "
        "Explain why this resume is a good match for the job description."
    )

    inputs = tokenizer(prompt, return_tensors="pt", max_length=256, truncation=True)
    outputs = model.generate(**inputs, max_new_tokens=80)
    explanation = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return explanation
