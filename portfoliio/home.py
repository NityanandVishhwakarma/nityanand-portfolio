import streamlit as st

st.set_page_config(page_title="Nityanand Vishwakarma | Portfolio", layout="wide")

# Header Section
st.title("Nityanand Vishwakarma 👋")
st.subheader("Aspiring Data Engineer | Python Developer | AI Enthusiast")

# Professional Summary
st.markdown("""
I am a **B.Tech Computer Science Engineering** graduate (2021) from **Lovely Professional University**[cite: 3, 35]. 
With a strong foundation in **Python, SQL, and ETL processes**, I specialize in building data pipelines 
and AI-integrated applications[cite: 4, 5, 8, 10]. 

I am passionate about transforming raw data into actionable intelligence through automation. 
My technical expertise includes **Apache Spark, Cloud Fundamentals, and Linux environments**, 
complemented by advanced certifications in Data Engineering and Data Science[cite: 5, 14, 23].
""")

st.divider()

# Core Skills Section (From your CV)
st.header("Technical Skills 🛠️")
col1, col2, col3 = st.columns(3)

with col1:
    st.write("**Languages & Core**")
    st.write("- Python & SQL [cite: 8, 10]")
    st.write("- Apache Spark [cite: 14]")
    st.write("- C++ [cite: 27]")

with col2:
    st.write("**Data Tools**")
    st.write("- Tableau & Excel [cite: 11, 12]")
    st.write("- Data Pipelines & ETL [cite: 9, 14]")
    st.write("- R Language [cite: 6]")

with col3:
    st.write("**CS Fundamentals**")
    st.write("- DBMS & OS [cite: 6]")
    st.write("- Computer Networks [cite: 6]")
    st.write("- Cloud Fundamentals [cite: 14]")