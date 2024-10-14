import streamlit as st
from utils.main import generate_job_description, generate_summary, extract_keywords

st.title("AI-Powered Job Description Generator")

job_title = st.text_input("Job Title")
company_name = st.text_input("Company Name")
brief_description = st.text_area("Brief Job Description")
desired_skills = st.text_area("Desired Skills (comma-separated)")
experience_level = st.selectbox("Experience Level", ["Entry-Level", "Mid-Level", "Senior"])
writing_style = st.selectbox("Writing Style", ["Formal", "Informal"])

# Generate Job Description
if st.button("Generate Job Description"):
    job_description = generate_job_description(job_title, company_name, brief_description, desired_skills, experience_level, writing_style)
    st.write("### Generated Job Description:")
    st.write(job_description)

   