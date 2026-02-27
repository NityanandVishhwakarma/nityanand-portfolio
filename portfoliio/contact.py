import streamlit as st

st.set_page_config(page_title="Contact Me", page_icon="📧")

st.title("Get In Touch 🤝")
st.write("If you have any questions or would like to collaborate on a project, feel free to reach out!")

# Two column layout for Contact Info and Form
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Contact Information")
    st.write("📍 **Location:** Maharajganj, Uttar Pradesh")
    st.write("📧 **Email:** nityanand8287@gmail.com") # [cite: 17]
    st.write("📞 **Phone:** +91 7973225589") # [cite: 16]
    st.write("🔗 **LinkedIn:** [Nityanand Vishwakarma](https://www.linkedin.com/in/nityanand-vishwakarma-16071016b/)") # [cite: 18, 19]
    
    st.write("---")
    st.write("Available for: **Data Analyst** or **Data Engineer** roles.")

with col2:
    st.subheader("Send a Message")
    # Note: Streamlit forms don't send emails natively. 
    # You can use 'Formsubmit.co' for a free email backend.
    contact_form = """
    <form action="https://formsubmit.co/nityanand8287@gmail.com" method="POST">
         <input type="text" name="name" placeholder="Your Name" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
         <input type="email" name="email" placeholder="Your Email" required style="width: 100%; padding: 10px; margin-bottom: 10px;">
         <textarea name="message" placeholder="Your Message" required style="width: 100%; padding: 10px; margin-bottom: 10px;"></textarea>
         <button type="submit" style="background-color: #007BFF; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">Send Message</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)

st.success("Tip: You can also reach out to me directly via LinkedIn for a faster response!")