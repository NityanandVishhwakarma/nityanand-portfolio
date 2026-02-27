import streamlit as st

st.set_page_config(page_title="Nityanand | Resume", layout="wide")

st.sidebar.title("💎 Portfolio Menu")
page = st.sidebar.radio("Navigate", ["Resume View", "Contact"])

# --- CSS (No Indentation inside the string) ---
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
@media print { [data-testid="stSidebar"], .stButton, header, footer { display: none !important; } .resume-wrapper { box-shadow: none; padding: 0; margin: 0; width: 100%; } .stApp { background: white !important; } }
</style>
""", unsafe_allow_html=True)

if page == "Resume View":
    
    resume_txt = "NITYANAND VISHWAKARMA\nData Engineer | AI Solutions Developer\nEmail: nityanand8287@gmail.com\nB.Tech LPU (2021)"
    st.download_button("📥 Download Resume (TXT)", data=resume_txt, file_name="Nityanand_Resume.txt", mime="text/plain")

    # --- HTML (No Indentation inside the string at all) ---
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
Highly analytical <b>B.Tech Graduate from LPU (2021)</b>. Expert in building <b>RAG-based AI applications</b>, <b>ETL pipelines</b>, and interactive <b>Power BI Dashboards</b>. Proficient in Python, SQL, and Streamlit for rapid data solution deployment.
</div>
<div class="res-title">Technical Projects & Impact</div>
<div class="res-entry-header"><span>UPSC SuperApp (NLP/RAG)</span> <span>Python | LangChain</span></div>
<div class="res-sub">Gen-AI Strategic Platform</div>
<div class="res-desc">
<ul>
<li>Developed a <b>Retrieval-Augmented Generation (RAG)</b> pipeline to process bulky PDF documents into structured study notes.</li>
<li>Implemented pattern analysis algorithms to identify high-frequency exam topics.</li>
<li><b>Outcome:</b> Streamlined note-taking for aspirants, automating document summarization with 90% accuracy.</li>
</ul>
</div>
<div class="res-entry-header"><span>Automated AI Data Analyst</span> <span>Gemini API | Pandas</span></div>
<div class="res-sub">Generative AI Business Solutions</div>
<div class="res-desc">
<ul>
<li>Built an automated EDA tool using <b>Google Gemini API</b> for natural language data insights.</li>
<li>Engineered dynamic chart generation logic using Streamlit.</li>
<li><b>Outcome:</b> Reduced initial data profiling time by over 70%.</li>
</ul>
</div>
<div class="res-entry-header"><span>VidiGraph AI</span> <span>Python | AI Models</span></div>
<div class="res-sub">Generative Media & Animation Tool</div>
<div class="res-desc">
<ul>
<li>Designed an innovative tool that transforms text-based prompts into engaging animated visual content.</li>
<li>Automated the graphics workflow by integrating specialized Python libraries.</li>
</ul>
</div>
<div class="res-entry-header"><span>Sales Performance Dashboard</span> <span>Power BI | SQL | DAX</span></div>
<div class="res-sub">Enterprise Business Intelligence</div>
<div class="res-desc">
<ul>
<li>Designed a comprehensive dashboard tracking regional revenue trends and sales health.</li>
<li>Developed complex <b>DAX measures</b> for Year-over-Year (YoY) performance monitoring.</li>
</ul>
</div>
<div class="res-title">Technical Skills</div>
<div style="margin-bottom: 10px;">
<span class="res-tag">Python (Pandas/NumPy)</span>
<span class="res-tag">SQL</span>
<span class="res-tag">Power BI</span>
<span class="res-tag">ETL Pipelines</span>
<span class="res-tag">Apache Spark</span>
<span class="res-tag">LangChain</span>
<span class="res-tag">Streamlit</span>
</div>
<div class="res-title">Education</div>
<div class="res-entry-header"><span>Lovely Professional University (LPU)</span> <span>2017 – 2021</span></div>
<div class="res-sub">B.Tech in Computer Science Engineering</div>
<div class="res-entry-header"><span>M.G. Inter College, Gorakhpur</span> <span>2016</span></div>
<div class="res-sub">Senior Secondary (Class XII) - UP Board</div>
<div class="res-title">Certifications</div>
<div class="res-desc">
<ul>
<li><b>Data Engineer</b> - Tutedude</li>
<li><b>Data Science</b> - Board Infinity</li>
<li><b>Data Structures & Algorithms</b> - University of San Diego</li>
<li><b>Software Engineering</b> - University of Alberta</li>
</ul>
</div>
</div>
"""
    st.markdown(html_content, unsafe_allow_html=True)
    st.info("🖨️ **PDF Download Tip:** Press **Ctrl + P** on your keyboard and select 'Save as PDF' to download the original formatted design.")

elif page == "Contact":
    st.title("Connect with Me 🤝")
    st.write("📧 **Email:** nityanand8287@gmail.com")