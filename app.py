# app.py

import streamlit as st
from datetime import datetime
from ai_logic import configure_api, generate_optimized_experience, generate_summary, generate_cover_letter
from doc_generator import create_professional_template, create_modern_template

st.set_page_config(page_title="AI Resume & Portfolio Builder", layout="wide")
client = configure_api()

if 'history' not in st.session_state:
    st.session_state.history = []

#  STREAMLIT FRONTEND 
st.title("🤖 AI-Resume & Portfolio Builder")
st.markdown("Enter your details below, and the AI will generate optimized content tailored to your target job.")

st.header("Enter Your Information")

col1, col2 = st.columns(2)
with col1:
    full_name = st.text_input("✍️ Full Name", placeholder="e.g., Jane Doe")
    email = st.text_input("📧 Email Address", placeholder="e.g., jane.doe@email.com")
    

with col2:
    phone_number = st.text_input("📞 Phone Number", placeholder="e.g., (123) 456-7890")
    linkedin_profile = st.text_input("🔗 LinkedIn Profile URL", placeholder="e.g., linkedin.com/in/janedoe")

target_job_title = st.text_input("🎯 Target Job Title", placeholder="e.g., Data Scientist")
skills = st.text_area("🛠️ Skills List (comma-separated)", placeholder="e.g., Python, SQL, Machine Learning, Team Leadership")
education = st.text_area("🎓 Education", height=100, placeholder="Enter your degree(s) and university.")
certifications = st.text_area("📜 Certifications", height=100, placeholder="Enter any relevant certifications.")
work_experience = st.text_area("🏆 Work Experience", height=300, placeholder="Enter your job duties and achievements for each role.\nFormat:\nProject Analyst - TechSolutions India, Bangalore (June 2022 - Present)\n\tCoordinated project activities for multiple software development teams using Agile methodologies.\n\tTracked project timelines, milestones, and deliverables in Jira, improving on-time task completion.\n\tFacilitated daily scrum meetings and prepared weekly status reports for stakeholders. ")

#  Template Selector 
template_choice = st.radio(
    "Select your desired resume template:",
    ("Professional", "Modern Two-Column"),
    horizontal=True
)

#  AI Generated Content Area 
st.header("Generated Documents")

if st.button("✨ Generate and Optimize Documents", type="primary"):
    if not all([full_name, email, phone_number, linkedin_profile, target_job_title, work_experience, education, skills, certifications]):
        st.warning("Please fill in all the fields to generate documents.")
    else:
        with st.spinner("Generating your Resume and Cover letter..."):
            st.session_state.optimized_experience = generate_optimized_experience(client, target_job_title, work_experience)
            st.session_state.optimized_summary = generate_summary(client, target_job_title, skills, work_experience, education)
            st.session_state.cover_letter = generate_cover_letter(client, full_name, target_job_title, st.session_state.optimized_summary, st.session_state.optimized_experience)
            st.session_state.app_ran = True

            history_entry = {
                "job_title": target_job_title,
                "summary": st.session_state.optimized_summary,
                "experience": st.session_state.optimized_experience,
                "cover_letter": st.session_state.cover_letter,
                "timestamp": datetime.now().strftime("%I:%M:%S %p")
            }
            st.session_state.history.insert(0, history_entry)

#  Display results 
if st.session_state.get('app_ran', False):
    st.subheader("📄 Optimized Resume Content")
    res_col1, res_col2 = st.columns(2)
    with res_col1:
        with st.expander("✅ Professional Summary", expanded=True):
            st.markdown(st.session_state.optimized_summary)
    with res_col2:
        with st.expander("✅ Work Experience", expanded=True):
            st.markdown(st.session_state.optimized_experience)

    st.subheader("✉️ Tailored Cover Letter")
    st.text_area("Editable Cover Letter", st.session_state.cover_letter, height=400)

    st.subheader("📥 Download Your Resume")
    try:
        if template_choice == "Professional":
            resume_bytes = create_professional_template(
            full_name=full_name, email=email, phone_number=phone_number, linkedin_profile=linkedin_profile,
            summary=st.session_state.optimized_summary, experience=st.session_state.optimized_experience,
            education=education, skills=skills, certifications=certifications,target_job_title=target_job_title
        )
        elif template_choice == "Modern Two-Column":
            resume_bytes = create_modern_template(full_name=full_name, email=email, phone_number=phone_number, linkedin_profile=linkedin_profile,
            summary=st.session_state.optimized_summary, experience=work_experience,
            education=education, skills=skills, certifications=certifications,target_job_title=target_job_title)
        
        st.download_button(
            label="Download Resume as .docx",
            data=resume_bytes,
            file_name=f"Resume_{full_name.replace(' ', '_')}.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
    except Exception as e:
        st.error(f"Failed to create download file: {e}")

#  SIDEBAR - Session History 
with st.sidebar:
    st.header("📜 Session History")
    if not st.session_state.history:
        st.info("Your generated documents from this session will appear here.")
    else:
        for i, entry in enumerate(st.session_state.history):
            with st.expander(f"Result {len(st.session_state.history) - i}: {entry['job_title']} ({entry['timestamp']})"):
                st.subheader("Summary")
                st.write(entry['summary'])
                st.subheader("Work Experience")
                st.write(entry['experience'])
                st.subheader("Cover Letter")
                st.write(entry['cover_letter'])
