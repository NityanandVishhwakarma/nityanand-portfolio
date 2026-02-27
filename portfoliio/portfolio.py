import streamlit as st
import os

# 1. Page Configuration
st.set_page_config(page_title="Nityanand | Data Portfolio", page_icon="📊", layout="wide")

# 2. Advanced Professional CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
    }

    /* --- SIDEBAR MENU HIGHLIGHTING --- */
    [data-testid="stSidebar"] {
        background-color: #000000 !important;
        border-right: 2px solid #00d2ff;
        min-width: 280px !important;
    }

    /* Sidebar Title & Labels */
    [data-testid="stSidebarNav"] {
        padding-top: 2rem;
    }

    /* Menu Text Highlight */
    .st-emotion-cache-17l774o { 
        font-size: 1.2rem !important; 
        font-weight: bold !important;
        color: #00d2ff !important;
    }

    /* HIGHLIGHT: Radio Button (Menu Item) Styling */
    div[data-testid="stSidebarUserContent"] .st-emotion-cache-162961g {
        background-color: rgba(0, 210, 255, 0.1);
        border: 1px solid rgba(0, 210, 255, 0.2);
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 5px;
        transition: all 0.3s ease;
    }

    /* Hover effect on Menu Items */
    div[data-testid="stSidebarUserContent"] .st-emotion-cache-162961g:hover {
        background-color: rgba(0, 210, 255, 0.3);
        transform: scale(1.05);
        border: 1px solid #00d2ff;
        box-shadow: 0px 0px 15px rgba(0, 210, 255, 0.4);
    }

    /* --- CONTENT BOX & HIGHLIGHTS --- */
    .content-box {
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #00d2ff;
        margin-bottom: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
        transition: 0.3s;
    }
    
    /* Project Card Hover */
    .content-box:hover {
        background: rgba(255, 255, 255, 0.12);
        border-left: 5px solid #92fe9d;
        transform: translateY(-5px);
    }

    h1, h2, h3 { color: #00d2ff !important; }
    .highlight { color: #92fe9d; font-weight: bold; text-shadow: 0px 0px 8px rgba(146, 254, 157, 0.5); }
    
    /* Input field styling */
    input, textarea {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 1px solid #00d2ff !important;
        border-radius: 5px !important;
    }
    </style>
    """, unsafe_allow_html=True)
# 3. Sidebar Navigation
st.sidebar.title("💎 Portfolio Menu")
# Added "Resume" to the navigation
page = st.sidebar.radio("Navigate", ["Home", "AI & Data Projects", "Resume", "Skills & Certs", "Feedback & Contact"])

# --- HOME PAGE ---
if page == "Home":
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        # CORRECTION 1: Path ko handle karne ke liye hamesha standard "/" use karein
        # Photo Section - Professional path handling
        photo_path = "C:/Users/acer/OneDrive/Desktop/portfoliio/myphoto.jpeg"
        
        if os.path.exists(photo_path):
            st.image(photo_path, use_container_width=True)
        else:
            # IMPROVEMENT: Photo na milne par placeholder ko thoda aur clean dikhaya hai
            st.markdown("""
                <div style='background:rgba(255,255,255,0.05); padding:60px; border-radius:15px; text-align:center; border: 1px dashed #00d2ff;'>
                    <h2 style='color:#00d2ff; margin:0;'>📸</h2>
                    <p style='color:#00d2ff; font-size:0.8em;'>Photo Placeholder</p>
                </div>
            """, unsafe_allow_html=True)
        
        # Education details with LPU highlight
        st.markdown("""
        <div class="college-tag" style="margin-top:20px;">
            <b style="color:#00d2ff;">🎓 Education</b><br>
            <b>B.Tech - Computer Science</b><br>
            Lovely Professional University (LPU)<br>
            <span style="font-size:0.9em;">Class of 2021</span>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Title with Gradient Effect and Animation
        st.markdown("""
            <h1 style='text-align: left; font-size: 3rem; margin-bottom: 0px;'>
                <span style='background: linear-gradient(to right, #00d2ff, #92fe9d); -webkit-background-clip: text; -webkit-text-fill-color: transparent;'>
                    Nityanand Vishwakarma
                </span>
            </h1>
        """, unsafe_allow_html=True)
        
        # Subheader with Typewriter feel or clean professional look
        st.markdown("""
            <h3 style='color: #e0e0e0; font-weight: 400; margin-top: -10px;'>
                Data Engineer <span style='color: #00d2ff;'>|</span> 
                Power BI Expert <span style='color: #00d2ff;'>|</span> 
                Python Developer
            </h3>
        """, unsafe_allow_html=True)
        
        # Visual Tech Stack Badges (Attractive icons substitute)
        st.markdown("""
            <div style="display: flex; gap: 10px; margin-top: 10px; margin-bottom: 20px;">
                <span style="background: rgba(0, 210, 255, 0.1); border: 1px solid #00d2ff; color: #00d2ff; padding: 2px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">⚡ ETL PIPELINES</span>
                <span style="background: rgba(146, 254, 157, 0.1); border: 1px solid #92fe9d; color: #92fe9d; padding: 2px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">📊 DAX & VISUALIZATION</span>
                <span style="background: rgba(255, 255, 255, 0.1); border: 1px solid #ffffff; color: #ffffff; padding: 2px 12px; border-radius: 20px; font-size: 0.8em; font-weight: bold;">🤖 GEN-AI & LLM</span>
            </div>
        """, unsafe_allow_html=True)

        # Aapka existing Attractive Intro yahan se start hoga
        st.markdown("""
        <div class="content-box">
            <h3 style="margin-top: 0; color: #00d2ff;">Bridging Data & AI with Streamlit 🚀</h3>
            <p style="line-height: 1.6;">
                I am a highly analytical <b>B.Tech Graduate</b> from <b>LPU</b> (2021) with a passion for data storytelling. 
                Specializing in <span class="highlight">Power BI, SQL, and Python</span>, I transform 
                complex raw data into interactive <b>Sales Dashboards</b> that drive business decisions.
            </p>
            <p style="line-height: 1.6;">
                Expert in building automated <b>ETL pipelines</b> and deploying <b>AI-integrated apps</b> 
                using <span class="highlight">Streamlit</span>. From the <b>'Automated AI Data Analyst'</b> to 
                <b>'UPSC SuperApp'</b>, I focus on creating scalable, intelligent, and user-friendly data solutions.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        st.success("🎯 Goal: Leveraging Cloud & AI to solve real-world data challenges.")
# --- PROJECTS PAGE ---
elif page == "AI & Data Projects":
    st.title("Technical Showcase 🚀")
    
    # 1. Visualization & Analytics
    st.header("📊 Visualization & Analytics")
    col_vis1, col_vis2 = st.columns(2)
    
    with col_vis1:
        st.markdown("""
        <div class="content-box">
            <h4>📈 Sales Performance Dashboard (Power BI)</h4>
            <p>A high-impact business intelligence solution designed to monitor enterprise sales health.</p>
            <ul>
                <li><b>Advanced ETL:</b> Leveraged <b>Power Query</b> to transform multi-source data into a structured star schema.</li>
                <li><b>Dynamic Calculations:</b> Implemented complex <b>DAX measures</b> for Year-over-Year (YoY) growth and MTD/YTD tracking.</li>
                <li><b>Stack:</b> Power BI, DAX, Power Query.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col_vis2:
        st.markdown("""
        <div class="content-box">
            <h4>🔍 Business Data Analytics (Excel & Tableau)</h4>
            <p>End-to-end analytical project focusing on data cleaning and visual storytelling.</p>
            <ul>
                <li><b>Data Wrangling:</b> Used <b>Advanced Excel</b> (Power Pivot) to consolidate disparate datasets.</li>
                <li><b>Visualization:</b> Built interactive <b>Tableau</b> dashboards for trend identification.</li>
                <li><b>Stack:</b> Excel, Tableau, VBA.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # 2. AI Innovations
    st.header("🤖 AI Innovations")
    
    # Automated AI Data Analyst
    st.markdown("""
    <div class="content-box">
        <h3>🧠 Automated AI Data Analyst <span class="ai-badge">GEN-AI</span></h3>
        <p><b>Objective:</b> To automate the repetitive Exploratory Data Analysis (EDA) phase using Gemini API.</p>
        <ul>
            <li><b>LLM Core:</b> Integrated <b>Google Gemini API</b> to act as a virtual consultant that explains data trends in natural language.</li>
            <li><b>Automated Visualization:</b> Developed logic that renders the most effective charts based on column statistics.</li>
            <li><b>Tech:</b> Python, Streamlit, Pandas, Google Generative AI.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # UPSC SuperApp
    st.markdown("""
    <div class="content-box">
        <h3>🎓 UPSC SuperApp <span class="ai-badge">NLP & RAG</span></h3>
        <p><b>Objective:</b> A strategic AI tool built specifically for civil services aspirants.</p>
        <ul>
            <li><b>Smart Summarization:</b> Built a RAG-based pipeline using <b>LangChain</b> to convert bulky PDFs into structured notes.</li>
            <li><b>Pattern Analysis:</b> Uses AI to analyze frequency of topics from previous years' papers.</li>
            <li><b>Tech:</b> Python, LangChain, PDFPlumber, Streamlit.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # VidiGraph AI
    st.markdown("""
    <div class="content-box">
        <h3>🎥 VidiGraph AI <span class="ai-badge">Generative Media</span></h3>
        <p><b>Objective:</b> To transform text-based prompts into engaging animated visual content.</p>
        <ul>
            <li><b>Dynamic Animation:</b> Uses Python libraries to generate automated graphics based on user input.</li>
            <li><b>Tech:</b> Python, Streamlit, AI Content Models.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- RESUME PAGE ---
elif page == "Resume":
    st.title("Professional Resume 📄")
    st.markdown("""
    <div class="content-box">
        <h3>Resume Overview</h3>
        <p>My resume covers my technical journey, including my <b>B.Tech from LPU</b>, core skills in <b>Data Engineering</b>, 
        and specialized projects in <b>AI and Business Intelligence</b>.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Path for your PDF
    resume_file = "C:/Users/acer/OneDrive/Desktop/portfoliio/Nityanand_Resume.pdf"
    
    if os.path.exists(resume_file):
        with open(resume_file, "rb") as f:
            pdf_bytes = f.read()
        st.download_button(
            label="📥 Download My Resume (PDF)",
            data=pdf_bytes,
            file_name="Nityanand_Vishwakarma_Resume.pdf",
            mime="application/pdf",
        )
    else:
        st.error("⚠️ Resume file 'Nityanand_Resume.pdf' not found. Please place it in your folder.")

# --- SKILLS PAGE ---
elif page == "Skills & Certs":
    st.title("Expertise & Qualifications 🎓")
    
    # 1. Technical Proficiency with Progress Bars
    st.subheader("Technical Proficiency")
    col_s1, col_s2 = st.columns(2, gap="large")
    
    with col_s1:
        st.write("🚀 **Streamlit (Full-stack Data Apps)**")
        st.progress(95)
        st.write("📊 **Power BI & Tableau**")
        st.progress(90)
        st.write("🐍 **Python (Pandas, Numpy)**")
        st.progress(85)
        
    with col_s2:
        st.write("📂 **SQL & ETL Pipelines**")
        st.progress(88)
        st.write("📗 **Advanced Excel**")
        st.progress(95)
        st.write("🤖 **AI (LangChain & Gemini API)**")
        st.progress(80)

    st.divider()

    # 2. Education & Certifications
    c1, c2 = st.columns(2, gap="medium")
    with c1:
        st.markdown(f"""
        <div class="content-box">
            <h3>🎓 Education</h3>
            <p><b>B.Tech - Computer Science Engineering</b> (2021)<br>
            Lovely Professional University (LPU), Punjab</p>
            <p><b>Senior Secondary</b> (2016)<br>
            M.G. Inter College, Gorakhpur</p>
            <p style="font-size: 0.9em; color: #92fe9d;">Focus: Data Engineering, Analytics, and AI Applications.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with c2:
        st.markdown(f"""
        <div class="content-box">
            <h3>🏆 Professional Certifications</h3>
            <ul style="line-height: 1.8;">
                <li><b>Data Engineer</b> - Tutedude</li>
                <li><b>Data Science</b> - Board Infinity</li>
                <li><b>DSA</b> - University of San Diego</li>
                <li><b>Software Engineering</b> - University of Alberta</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    # 3. Core Competencies (Bonus Section)
    st.subheader("Core Competencies")
    st.markdown("""
    <div style="display: flex; flex-wrap: wrap; gap: 10px;">
        <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid #00d2ff; padding: 5px 15px; border-radius: 20px;">Data Modeling</span>
        <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid #00d2ff; padding: 5px 15px; border-radius: 20px;">ETL Pipelines</span>
        <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid #00d2ff; padding: 5px 15px; border-radius: 20px;">Generative AI</span>
        <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid #00d2ff; padding: 5px 15px; border-radius: 20px;">Statistical Analysis</span>
        <span style="background: rgba(0, 210, 255, 0.2); border: 1px solid #00d2ff; padding: 5px 15px; border-radius: 20px;">Dashboard Automation</span>
    </div>
    """, unsafe_allow_html=True)
    
    
    # --- FEEDBACK & CONTACT PAGE ---
elif page == "Feedback & Contact":
    st.title("Connect & Feedback 🤝")
    col_a, col_b = st.columns(2)
    
    with col_a:
        st.markdown("""
        <div class="content-box">
            <h3>Contact Details</h3>
            <p>📧 <b>Email:</b> nityanand8287@gmail.com</p>
            <p>📞 <b>Phone:</b> +91 7973225589</p>
            <p>🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/nityanand-vishwakarma-16071016b/" style="color:#00d2ff;" target="_blank">Visit Profile</a></p>
        </div>
        """, unsafe_allow_html=True)

    with col_b:
        st.subheader("Send Live Feedback")
        feedback_form = """
        <form action="https://formsubmit.co/nityanand8287@gmail.com" method="POST">
            <input type="text" name="name" placeholder="Your Name" required style="width:100%; margin-bottom:10px; padding:10px;">
            <input type="email" name="email" placeholder="Your Email" required style="width:100%; margin-bottom:10px; padding:10px;">
            <textarea name="message" placeholder="Your Message" required style="width:100%; height:100px; margin-bottom:10px; padding:10px;"></textarea>
            <button type="submit" style="background:#00d2ff; color:black; border:none; padding:10px 20px; border-radius:5px; font-weight:bold; cursor:pointer; width:100%;">Send Message</button>
        </form>
        """
        st.markdown(feedback_form, unsafe_allow_html=True)