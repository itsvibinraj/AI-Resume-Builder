# ai_logic.py

import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

def configure_api():
    try:
        api_key = st.secrets.get("GROQ_API_KEY")
        if not api_key:
            api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("API key not found. Make sure it's set in your .env file.")
        client = Groq(api_key=api_key)
        return client
    except Exception as e:
        st.error(f"Error configuring API: {e}")
        st.stop()

def generate_optimized_experience(client, job_title, work_experience):
    
    prompt = f"""
    You are an expert career advisor and resume writer with 20 years of experience.

Your task is to rewrite and enhance ONLY the achievement bullet points under each job title in the provided work experience. You MUST PRESERVE the original job titles, company names, locations, and dates exactly as they are written.

**Instructions for rewriting bullet points:**
1.  Use strong action verbs and quantify results with numbers or metrics (e.g., "increased efficiency by 15%").
2.  Apply the STAR method (Situation-Task-Action-Result) where possible.
3.  Tailor the language and keywords to align with the **Target Job Title: {job_title}**.

**Strict Formatting Rules:**
- Your response must contain ONLY the rewritten work experience section.
- Do not add any introductory or concluding sentences like "Here are the rewritten bullet points...".

**Example:**

**User Input:**
`Project Analyst - TechSolutions India (June 2022 - Present)
- Coordinated project activities.
- Tracked timelines and deliverables in Jira.
- Facilitated daily meetings.`

**Your Desired Output:**
`Project Analyst - TechSolutions India, Bangalore (June 2022 - Present)
- Coordinated project activities for multiple software development teams using Agile methodologies.
- Tracked project timelines, milestones, and deliverables in Jira, improving on-time task completion by 15%.
- Facilitated daily scrum meetings and prepared weekly status reports for stakeholders.`

---

Now, rewrite the following work experience based on all the rules above:

**Work Experience to Rewrite:**
{work_experience}"""
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while generating experience points: {e}"

def generate_summary(client, job_title, skills, work_experience, education):
    """Generates a professional resume summary from all inputs."""
    prompt = f"""
    Based on the following comprehensive information, write a compelling and professional resume summary of 3-4 lines.

    **Target Job Title:** {job_title}
    **Key Skills:** {skills}
    **Work Experience Highlights:** {work_experience}
    **Education:** {education}

    **Instructions:**
    -   Synthesize all the provided information into a brief, compelling narrative for the top of a resume.
    -   Start with a strong, descriptive title that aligns with the target job (e.g., "Results-driven Data Scientist" or "Innovative Software Engineer").
    -   Incorporate high-value keywords from the skills list and reflect the experience and education provided.
    -   No need on any title or heading, just the summary text.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while generating the summary: {e}"

def generate_cover_letter(client, full_name, job_title, optimized_summary, optimized_experience):
    """Generates a tailored cover letter."""
    prompt = f"""
    Write a professional and tailored one-page cover letter.

    **Applicant's Name:** {full_name}
    **Target Job Title:** {job_title}
    **Optimized Resume Summary for Context:**
    {optimized_summary}
    **Optimized Experience Bullet Points for Context:**
    {optimized_experience}

    **Instructions:**
    1.  **Structure:** 3-4 paragraphs (Introduction, Body, Conclusion with a call to action).
    2.  **Sign-off:** The sign-off must be "Sincerely," followed by the applicant's name: {full_name}.
    """
    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred while generating the cover letter: {e}"
