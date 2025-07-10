import streamlit as st
from config import call_gemini, show_sidebar
from prompts import resume_prompt

# from docx import Document
# from io import BytesIO

# import pdfkit
# from io import BytesIO


show_sidebar()

st.title("📄 Resume Builder")
# st.markdown("Build and refine your resume with AI assistance.")

st.write("🔍 Session State Debug:", st.session_state)

# Check if user is logged in
if "user" not in st.session_state:
    st.error("You need to log in to use the Resume Builder.")
    st.stop()

else:
    user = st.session_state["user"]

st.markdown(f"Welcome **{user['name']}**, let's build your resume.")
st.markdown("Please fill in the details below to generate your personalized resume.")
st.markdown("Leave this field blank to get a generic resume template.")


with st.form("resume_form"):
    phone = st.text_input("📞 Phone")
    email = st.text_input("📩 Email")
    summary = st.text_area("🗒️ Professional Summary")
    skills = st.text_area("💡 Skills (comma-separated)")
    experience = st.text_area("💼 Work Experience")
    certifications = st.text_area("🎓 Certifications (optional)")

    submit = st.form_submit_button("✨ Generate Resume")

if submit:
    st.session_state["user_resume_data"] = {
        "name": user["name"],
        "experience_level": user["experience"],
        "education": user["education"],
        "phone": phone,
        "email": email,
        "summary": summary,
        "skills": skills,
        "experience": experience,
        "certifications": certifications or "None"
    }
    st.write("Session User Info:", st.session_state.user_resume_data)

    prompt = resume_prompt()

    with st.spinner("Generating your resume..."):
        resume = call_gemini(prompt)

    st.success("✅ Resume generated successfully!")
    st.markdown("### 📝 Your Resume")
    st.write(resume)


    
# Function to export resume as PDF or Word
# Comment these out later
# def export_as_pdf(resume_text):
#     pdf = pdfkit.from_string(resume_text, False)
#     st.download_button(
#         label="Download PDF",
#         data=pdf,
#         file_name="resume.pdf",
#         mime="application/pdf"
#     )

# def export_as_word(resume_text):
#     doc = Document()
#     doc.add_heading('Resume', level=1)
#     for line in resume_text.split('\n'):
#         doc.add_paragraph(line)
    
#     buffer = BytesIO()
#     doc.save(buffer)
#     buffer.seek(0)

#     st.download_button(
#         label="Download Word Document",
#         data=buffer,
#         file_name="resume.docx",
#         mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
#     )

# Buttons for exporting the resume
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("📄 Export as PDF"):
#         export_as_pdf(st.session_state.generated_resume)
# with col2:
#     if st.button("📝 Export as Word"):
#         export_as_word(st.session_state.generated_resume)

# Expanding section for refining specific parts of the resume
with st.expander("💡 Ask to Improve This Section"):
    section_input = st.text_area("Paste the section you'd like to refine")
    if st.button("Refine Section"):
        improved = call_gemini(f"Please refine this section professionally:\n{section_input}")
        st.markdown("### ✨ Refined Section")
        st.markdown(improved)