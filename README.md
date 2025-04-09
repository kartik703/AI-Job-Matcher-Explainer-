---
title: AI Job Match Explainer
emoji: 💼
colorFrom: indigo
colorTo: pink
sdk: streamlit
sdk_version: "1.32.0"
app_file: app.py
pinned: false
license: mit
---

# 💼 AI Job Match Explainer

[![Hugging Face Space](https://img.shields.io/badge/🤗%20Try%20on%20Hugging%20Face-blue?logo=huggingface)](https://huggingface.co/spaces/kartikG2000/AI_Job_matcher)

**Smart NLP tool to analyze how well your resume matches a job description** — with match score, keyword highlights, and a GPT-style explanation using `flan-t5-base`.

---

## 🚀 Live Demo

🧠 **Try it now →** [https://huggingface.co/spaces/kartikG2000/AI_Job_matcher](https://huggingface.co/spaces/kartikG2000/AI_Job_matcher)

---

## 📋 Features

✅ Upload your **resume** (PDF or TXT)  
✅ Paste any **job description**  
✅ Extract **JD keywords** with KeyBERT  
✅ Calculate a **hybrid match score**:
- 70% cosine similarity (TF-IDF)
- 30% fuzzy keyword overlap  
✅ 🧠 Get GPT-style reasoning with `flan-t5-base`  
✅ 📊 View match score chart  
✅ 📄 Download a custom PDF report

---

## 🧠 Powered By

| Feature            | Tool/Model                |
|--------------------|---------------------------|
| UI                 | Streamlit                 |
| Resume Parsing     | pdfplumber, docx          |
| JD Keywords        | KeyBERT                   |
| NLP + Cleaning     | spaCy, scikit-learn       |
| Explanation Model  | `google/flan-t5-base`     |
| Visualization      | Matplotlib                |
| Report Export      | FPDF                      |

---


---

## 💻 Run Locally

```bash
git clone https://github.com/kartik703/AI-Job-Matcher-Explainer-.git
cd AI-Job-Matcher-Explainer-
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py


🧪 Example Use Case

Job Description: Looking for candidates with Python, machine learning, cloud, and consulting
Resume Contains: Python, AWS cloud, data science, client-facing
Match Score: 87.5%
Explanation:

“This resume includes key technical skills (Python, cloud), relevant work experience (consulting), and overlaps with most core JD requirements.”

👨‍💻 Author

Built with ❤️ by Kartik Goswami
📬 Open to collaborations, internships, and roles in AI, ML, or data science.