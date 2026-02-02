import streamlit as st
import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="Care Bridge Initiatives", layout="wide")

# Sidebar Menu
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to:",
    ["Home", "Projects", "Skills", "Contact"],
)

# Care Bridge Initiative Project Data
projects_data = {
    "AI Nursing Chatbot": {
        "Stage": "Prototype",
        "Impact": 80
    },
    "MedAssistBot": {
        "Stage": "Concept",
        "Impact": 70
    },
    "Ethical AI Framework": {
        "Stage": "Research",
        "Impact": 90
    }
}


# Sections based on menu selection
if menu == "Home":
    st.title("Care Bridge Initiatives")
    
    st.write("""Care Bridge Initiatives explores how ethical, human-centered artificial intelligence can support healthcare education, clinical decision-making, and patient wellbeing. This project brings together technology,design,and empathy to create digital tools that place people at the center of innovation. 

My work focuses on conversational AI systems that help users feel informed, supported, and safe — especially 
in sensitive healthcare contexts. Through research, prototyping, and user-centered design methods, I aim to 
develop solutions that are not only technically effective, but also emotionally aware and socially responsible.""")
    
    st.markdown("### Mission")

    st.write("""
To design trustworthy, empathetic AI tools that bridge the gap between technology and care.
    """)

    st.markdown("### What I Work On")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("#### 🧠 Ethical AI")
        st.write("""My work in Ethical AI focuses on responsible system design, fairness, transparency, and privacy. 
I explore how AI systems can be built with accountability in mind, ensuring users understand how 
decisions are made while protecting sensitive data. This includes considering bias, consent, and 
human oversight when developing healthcare-focused technologies.""")

    with col2:
        st.markdown("#### 🏥 Healthcare")
        st.write("""I investigate how digital tools can support clinical learning, nursing education, and patient safety. 
My projects aim to improve access to information, reduce reporting barriers, and enhance care experiences 
through AI-driven assistance. I am particularly interested in how technology can empower both healthcare 
professionals and patients.""")

    with col3:
        st.markdown("#### 🤖 Conversational Systems")
        st.write("""I design and prototype conversational AI systems that prioritize empathy, clarity, and cultural sensitivity. 
These chatbots are built to provide emotional support alongside accurate information, helping users navigate 
health-related challenges while feeling heard and respected.""")

    st.markdown("### About Me")
    col1, col2 = st.columns([1, 3])

with col1:
       st.image("C:/Users/zahir/Downloads/copy_5754A7B4-0233-410F-9DDE-02B294EF5192.png", width=140)

with col2:

    st.write("""
I am Sasha-Leigh Allen, a University of the Western Cape (UWC) student pursuing a BCom (General) degree, 
majoring in Information Systems and Finance.

I am passionate about exploring how technology and data can be used to solve real-world problems, 
particularly in healthcare and social impact spaces. My interests lie at the intersection of artificial 
intelligence, user-centered design, and business strategy — where innovation meets empathy.

Through my projects, I focus on building conversational AI tools and digital solutions that are ethical, 
practical, and human-centered. I enjoy turning complex ideas into simple, meaningful experiences, and I am 
constantly learning how to bridge the gap between technology, finance, and care.

I aspire to grow into a role where I can contribute to impactful tech-driven solutions while continuing to 
develop my skills in AI, product design, and data-informed decision-making.
    """)



if menu == "Projects":
    st.title("Projects")

    project = st.selectbox(
        "Choose a project",
        ["AI Nursing Chatbot", "HIV Self-Care Chatbot", "Ethical AI Framework"]
    )

 # Create two columns for project content
    col1, col2 = st.columns([3, 1])  # left column is wider

    if project == "AI Nursing Chatbot":
        with col1:
          st.subheader("AI Nursing Chatbot")

          st.write("""
This project investigates how conversational artificial intelligence can support nursing students in clinical 
learning environments. Through preliminary research, it became evident that many nursing students struggle to 
report clinical incidents clearly and confidently, often due to fear of making mistakes or uncertainty about 
formal reporting procedures.

The primary objective of this project was to design a chatbot-based system that guides students step-by-step 
through incident reporting while reinforcing learning outcomes. Using user interviews and empathy mapping, I 
gathered insights into student experiences and emotional challenges. These findings informed the development 
of a prototype built in Streamlit.

The outcome was an interactive chatbot that assists users in documenting incidents in a structured and 
supportive manner. This project demonstrated how AI-driven tools can improve usability, promote patient safety, 
and enhance confidence in clinical education.
        """)
# -------------------------------------------------------
if menu == "Projects":
    st.title("Projects")

    project = st.selectbox(
        "Choose a project",
        ["AI Nursing Chatbot", "HIV Self-Care Chatbot", "Ethical AI Framework"]
    )

    # Define two columns inside the Projects block
    col1, col2 = st.columns([3, 1])

    if project == "AI Nursing Chatbot":
        with col1:
            st.subheader("AI Nursing Chatbot")
            st.write("""
This project investigates how conversational artificial intelligence can support nursing students in clinical 
learning environments. Through preliminary research, it became evident that many nursing students struggle to 
report clinical incidents clearly and confidently, often due to fear of making mistakes or uncertainty about 
formal reporting procedures.

The primary objective of this project was to design a chatbot-based system that guides students step-by-step 
through incident reporting while reinforcing learning outcomes. Using user interviews and empathy mapping, I 
gathered insights into student experiences and emotional challenges. These findings informed the development 
of a prototype built in Streamlit.

The outcome was an interactive chatbot that assists users in documenting incidents in a structured and 
supportive manner. This project demonstrated how AI-driven tools can improve usability, promote patient safety, 
and enhance confidence in clinical education.
            """)

        with col2:
            st.markdown("**Stage:** Prototype")
            st.markdown("**Impact:** 80%")

    elif project == "HIV Self-Care Chatbot":
        with col1:
            st.subheader("HIV Self-Care Chatbot")
            st.write("""
This project focuses on addressing the lack of accessible, trustworthy, and empathetic digital support for 
young adults living with HIV. Research revealed that while many individuals are comfortable using technology, 
they often hesitate to engage with digital health platforms due to concerns about privacy, misinformation, 
and emotional understanding.

The goal of this project was to design a conversational AI system that provides accurate health information 
while also offering emotional support and culturally sensitive communication. The system emphasizes privacy-first 
design and personalized educational content to encourage engagement and self-care.

The resulting prototype highlights the importance of trust in digital health environments. By combining 
empathetic dialogue with reliable information, the chatbot supports users in managing their wellbeing while 
fostering a sense of dignity and autonomy.
            """)

        with col2:
            st.markdown("**Stage:** Concept")
            st.markdown("**Impact:** 70%")

    elif project == "Ethical AI Framework":
        with col1:
            st.subheader("Ethical AI Framework")
            st.write("""
This research project explores ethical considerations in healthcare artificial intelligence, with particular 
attention to fairness, accountability, transparency, and data privacy. The study examines how AI systems can be 
designed responsibly to protect sensitive patient information while maintaining clarity around automated 
decision-making processes.

The framework emphasizes the importance of human oversight, informed consent, and responsible deployment of 
AI technologies in clinical contexts. This work reflects my interest in ensuring that innovation in healthcare 
remains aligned with social values and patient trust.
            """)

        with col2:
            st.markdown("**Stage:** Research")
            st.markdown("**Impact:** 90%")

# -------------------------------------------------------


elif  menu == "Skills":
      st.header("Skills & Tools")
      col1, col2 = st.columns(2)

      with col1:
       st.write("""
My technical skill set includes Python programming, Streamlit application development, and the design of 
conversational AI systems. I also have experience working with data for analysis and prototyping, allowing 
me to translate conceptual ideas into functional digital solutions. 
        """)

      with col2:
       st.markdown("""
My research and design capabilities are grounded in user-centered methodologies such as UX research, empathy 
mapping, and user interviews. I place strong emphasis on ethical considerations in AI development and apply 
product thinking principles to ensure that solutions are both practical and socially responsible.
        """)


if menu == "Contact":
    # Add a contact section
    st.header("Contact Information")
    email = "sasha.allen@example.com"
    st.write(f"You can reach me at {email}.") 
    st.markdown("This page represents my journey into ethical AI and healthcare innovation.")