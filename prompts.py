import streamlit as st
user_resume_data = st.session_state.get("user_resume_data", {})

def resume_prompt(user_resume_data: dict) -> str:
    return f"""
    Using the following details, generate a clean and professional resume in plain text:
    
    {user_resume_data}

    Keep formatting readable and suitable for PDF or Word export.
    """


def extract_prompt(job_description: str) -> str:
    return f"""
    Analyze the following job description and extract:
    - Required experience level
    - Core and soft skills
    - Responsibilities
    - Keywords to use in CV/resume/cover letter

    Job Description:
    {job_description}

    Return the extracted information using an easy to understand format, e.g., bullet points, not complicated to an average reader.
    """

def analyze_prompt(user: dict, job_description: str) -> str:
    return f"""
    Evaluate this user's suitability for the job description below. Give a percentage match score and justify it in a short paragraph. Also, provide suggestions for improving their CV/resume/cover letter to better fit the job.
    Give a score out of 100. This number will be used in a progress bar.
    --- USER PROFILE ---
    Name: {user['name']}
    Experience: {user['experience']}
    Education: {user['education']}
    Skills: {user_resume_data.get('skills')}
    Summary: {user_resume_data.get('summary')}
    Work Experience: {user_resume_data.get('experience')}
    Certifications: {user_resume_data.get('certifications', 'None')}

    --- JOB DESCRIPTION ---
    {job_description}

    Return your response in this format:
    Score: <number>
    Justification: <short paragraph>
    Suggestions: <bulleted list or short paragraph>
    All on different lines.

    """   