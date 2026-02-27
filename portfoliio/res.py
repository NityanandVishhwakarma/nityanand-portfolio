import streamlit as st

st.set_page_config(page_title="Nityanand | Resume", layout="wide")

st.sidebar.title("💎 Portfolio Menu")
page = st.sidebar.radio("Navigate", ["Resume View", "Contact"])

# --- CSS (Strictly formatted to prevent Streamlit Markdown errors) ---
st.markdown("""
<style>
.stApp { background-color: #f4f6f9; color: #333; font-family: 'Segoe UI', Tahoma, sans-serif; }
.resume-wrapper { max-width: 900px; margin: auto; padding: 50px; background: #ffffff; border-radius: 8px; box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.08); }
.res-header { text-align: center; border-bottom: 3px solid #0056b3; padding-bottom: 20px; margin-bottom: 25px; }
.res-name { font-size: 36px; font-weight: 900; color: #1a1a1a; letter-spacing: 1px; }
.res-contact { font-size: 15px; color: #555; margin-top: 10px; }
.res-contact a { color: #0056b3; text-decoration: none; font-weight: 600; }
.res-title { background: #eef2f7; color: #0056b3; padding: 10px 15px; font-size: 16px; font-weight: 800; text-transform: uppercase; border-left: 5px solid #0056b3; margin: 30px 0 15px 0; }
.res-entry-header { display: flex; justify-content: space-between; font-weight: 800; font-size: 17px; margin-top: 20px; color: #222; }
.res-sub { font-style: italic; color: #0056b3; font-size: 14px; margin-bottom: 8px; font-weight: 600;}
.res-desc { font-size: 15px; color: #444; line-height: 1.6; margin-bottom: 10px; }
.res-desc ul { margin-top: 5px; padding-left: 20px; }
.res-desc li { margin-bottom: 5px; }
.res-tag { display: inline-block; background: #f8f9fa; color: #333; padding: 6px 14px; border-radius: 20px; font-size: 14px; font-weight: 600; margin: 0 8px 10px 0; border: 1px solid #d1d9e4; }
.highlight-text { background-color: #e6f2ff; padding: 2px 6px; border-radius: 4px; font-weight: 600; color: #0056b3; }
@media print { [data-testid="stSidebar"], .stButton, header, footer { display: none !important; } .resume-wrapper { box-shadow: none; padding: 0; margin: 0; width: 100%; } .stApp { background: white !important; } }
</style>
""", unsafe_allow_html=True)

if page == "Resume View":
    
    resume_txt = "NITYANAND VISHWAKARMA\nData Engineer | AI Solutions Developer\nEmail: nityanand8287@gmail.com\nB.Tech LPU (2021)"
    st.download_button("📥 Download ATS-Friendly Resume (TXT)", data=resume_txt, file_name="Nityanand_Resume.txt", mime="text/plain")

    # --- HTML Structure ---
    html_content = """
<div class="resume-wrapper">
<div class="res-header">
<div class="res-name">NITYANAND VISHWAKARMA</div>
<div class="res-contact">
📧 nityanand8287@gmail.com | 📞 +91 7973225589 | 📍 Maharajganj, UP <br>
🔗 <a href="https://www.linkedin.com/in/nityanand-vishwakarma-16071016b/" target="_blank">LinkedIn Profile</a>
</div>
</div>

<div class="res-title">Professional Summary</div>
<div class="res-desc">
Analytical and detail-oriented <b>B.Tech CS Graduate (LPU 2021)</b>. Successfully translated intensive research discipline and complex pattern-recognition skills developed during civil services preparation into building highly optimized <b>Data Engineering pipelines</b> and <b>Generative AI solutions</b>. Specializing in RAG-based architectures, ETL processes, and creating actionable business intelligence dashboards using Power BI and Streamlit.
</div>

<div class="res-title">Independent Development & AI Projects</div>

<div class="res-entry-header"><span>UPSC SuperApp (NLP/RAG)</span> <span>Python | LangChain | ChromaDB</span></div>
<div class="res-sub">Gen-AI Strategic Platform (Current)</div>
<div class="res-desc">
<ul>
<li>Engineered a <span class="highlight-text">Retrieval-Augmented Generation (RAG)</span> pipeline to process and query bulky academic PDF documents into structured study notes.</li>
<li>Developed a pattern analysis engine to scan historical exam datasets, identifying high-frequency topics for strategic preparation.</li>
<li><b>Business Impact:</b> Automated 100% of manual document summarization, delivering context-aware answers with 90%+ accuracy.</li>
</ul>
</div>

<div class="res-entry-header"><span>Automated AI Data Analyst</span> <span>Google Gemini API | Pandas | Streamlit</span></div>
<div class="res-sub">Self-Service BI Application</div>
<div class="res-desc">
<ul>
<li>Architected an automated Exploratory Data Analysis (EDA) tool leveraging the <b>Gemini API</b> to translate raw CSV datasets into natural language insights.</li>
<li>Implemented dynamic, user-driven chart generation logic, allowing non-technical stakeholders to visualize complex data instantly.</li>
<li><b>Business Impact:</b> Reduced initial data profiling and reporting turnaround time by over <span class="highlight-text">70%</span>.</li>
</ul>
</div>

<div class="res-entry-header"><span>Sales Performance Dashboard</span> <span>Power BI | SQL | Power Query</span></div>
<div class="res-sub">Enterprise Data Visualization</div>
<div class="res-desc">
<ul>
<li>Designed an end-to-end dashboard tracking regional revenue trends by performing robust <b>ETL transformations</b> (Star Schema modeling).</li>
<li>Authored advanced <span class="highlight-text">DAX measures</span> to calculate Year-over-Year (YoY) growth and MTD/YTD performance metrics.</li>
</ul>
</div>

<div class="res-entry-header"><span>VidiGraph AI</span> <span>Python | AI Media Models</span></div>
<div class="res-sub">Generative Media Engine</div>
<div class="res-desc">
<ul>
<li>Developed an automated graphics workflow using specialized Python libraries to convert text-based data prompts into animated visual content for digital storytelling.</li>
</ul>
</div>

<div class="res-title">Technical Expertise</div>
<div style="margin-bottom: 10px;">
<span class="res-tag">Python (Pandas, NumPy)</span>
<span class="res-tag">Advanced SQL</span>
<span class="res-tag">Power BI & DAX</span>
<span class="res-tag">ETL Pipelines</span>
<span class="res-tag">LangChain & LLMs</span>
<span class="res-tag">Streamlit</span>
<span class="res-tag">Data Modeling</span>
</div>

<div class="res-title">Education</div>
<div class="res-entry-header"><span>Lovely Professional University (LPU), Phagwara</span> <span>2017 – 2021</span></div>
<div class="res-sub">B.Tech in Computer Science Engineering</div>

<div class="res-title">Professional Certifications</div>
<div class="res-desc">
<ul>
<li><b>Data Engineering Certification</b> - Tutedude</li>
<li><b>Data Science Specialization</b> - Board Infinity</li>
<li><b>Data Structures & Algorithms</b> - University of San Diego</li>
<li><b>Software Engineering</b> - University of Alberta</li>
</ul>
</div>
</div>
"""
    st.markdown(html_content, unsafe_allow_html=True)
    st.info("💡 **Pro Tip for Recruiters:** Press **Ctrl + P** and select 'Save as PDF' to download this perfectly formatted version.")

elif page == "Contact":
    st.title("Let's Build Data Solutions 🤝")
    st.write("I am actively looking for Data Engineer and Data Analyst roles. Let's connect!")
    st.write("📧 **Email:** nityanand8287@gmail.com")
    st.write("🔗 **LinkedIn:** [Visit My Profile](https://www.linkedin.com/in/nityanand-vishwakarma-16071016b/)")