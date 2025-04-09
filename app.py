# app.py

import streamlit as st
from resume_parser import extract_text_from_resume
from jd_parser import extract_keywords_from_jd
from matcher import compute_combined_score
from explanation import generate_explanation
from fpdf import FPDF
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="AI Job Match Explainer", layout="centered")
st.title("💼 AI Job Match Explainer")

st.markdown("Upload your resume and paste the job description to check your fit for the role!")

uploaded_file = st.file_uploader("📄 Upload Resume (PDF or TXT)", type=["pdf", "txt"])
jd_text = st.text_area("📋 Paste Job Description", height=200)

if st.button("🔍 Match Now"):
    if uploaded_file and jd_text:
        file_ext = uploaded_file.name.split(".")[-1]
        temp_path = f"temp_resume.{file_ext}"

        with open(temp_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        resume_text = extract_text_from_resume(temp_path)
        jd_keywords = extract_keywords_from_jd(jd_text, top_n=10)
        similarity, matched_keywords = compute_combined_score(resume_text, jd_text, jd_keywords)

        st.success(f"🔗 Match Score: **{similarity}%**")

        st.markdown("**🧠 Extracted JD Keywords:**")
        st.markdown(", ".join(f"`{kw}`" for kw in jd_keywords) if jd_keywords else "No keywords found.")

        st.markdown("**📌 Matching Keywords Found in Resume:**")
        st.markdown(", ".join(f"`{kw}`" for kw in matched_keywords) if matched_keywords else "_None matched_.")

        with st.spinner("Generating GPT-style explanation..."):
            explanation = generate_explanation(jd_keywords, matched_keywords)
            st.markdown("**🧠 GPT-Style Explanation:**")
            st.info(explanation)

        st.markdown("### 📊 Match Score Visualization")
        fig, ax = plt.subplots()
        ax.barh(["Match Score"], [similarity])
        ax.set_xlim(0, 100)
        ax.set_xlabel("Percentage")
        st.pyplot(fig)

        st.markdown("### 📄 Download Match Report")

        if st.button("📥 Generate PDF Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)

            pdf.cell(200, 10, txt="AI Job Match Report", ln=True, align="C")
            pdf.ln(10)
            pdf.cell(200, 10, txt=f"Match Score: {similarity}%", ln=True)

            pdf.ln(5)
            pdf.multi_cell(0, 10, txt="Extracted JD Keywords:\n" + ", ".join(jd_keywords))
            pdf.ln(5)
            pdf.multi_cell(0, 10, txt="Matched Keywords in Resume:\n" + ", ".join(matched_keywords))
            pdf.ln(5)
            pdf.multi_cell(0, 10, txt="Explanation:\n" + explanation)

            pdf.output("match_report.pdf")
            with open("match_report.pdf", "rb") as f:
                st.download_button("⬇️ Download Report", f, file_name="match_report.pdf")

        os.remove(temp_path)
    else:
        st.error("Please upload a resume and paste a job description.")
