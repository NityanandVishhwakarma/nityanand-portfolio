import streamlit as st

st.title("My Projects 🚀")

# 1. Automated AI Data Analyst
with st.expander("📊 Automated AI Data Analyst", expanded=True):
    st.write("""
    - Developed a specialized tool using **Streamlit and Google Gemini API** to automate Exploratory Data Analysis (EDA).
    - Built features for intelligent insight generation and automated visualization from uploaded datasets.
    """)

# 2. UPSC SuperApp
with st.expander("🎓 UPSC SuperApp"):
    st.write("""
    - Created an AI-driven platform leveraging **LangChain** to assist aspirants in generating structured notes from PDFs.
    - Integrated strategic data insights to help users optimize their preparation and exam strategy.
    """)

# 3. VidiGraph AI
with st.expander("🎥 VidiGraph AI"):
    st.write("""
    - An innovative Generative AI project using Python to convert text prompts into animated visual content.
    """)

# 4. Academic Projects (From CV)
with st.expander("🏫 Scholarship Management System"):
    st.write("- Designed a system in **C++** to calculate student scholarships based on academic criteria[cite: 27, 28].")
    st.write("- Implemented efficient data structures for fast processing and clarity[cite: 29].")

with st.expander("🏥 Hospital Management System"):
    st.write("- Developed a web-based platform providing hospital details and doctor availability[cite: 42, 44].")
    st.write("- Tech Stack: HTML, CSS, JavaScript[cite: 45].")