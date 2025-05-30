import streamlit as st
import PyPDF2
import requests
import json

# Configure the Gemini API
GEMINI_API_KEY = "AIzaSyCKmqTc-_ozylHj88yXs-8qV8HUzzbUHk0"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def extract_text_from_pdf(pdf_file):
    """Extract text from uploaded PDF file."""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

def analyze_resume(resume_text):
    """Analyze resume using Gemini API and return score and recommendation."""
    prompt = f"""
    Analyze this resume and provide ONLY:
    1. A score from 1-100
    2. A clear "ACCEPT" or "REJECT" decision
    
    Resume:
    {resume_text}
    
    Format your response exactly as:
    SCORE: [number]/100
    DECISION: [ACCEPT/REJECT]
    """
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [{
            "parts": [{
                "text": prompt
            }]
        }]
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    response_data = response.json()
    
    if 'candidates' in response_data and len(response_data['candidates']) > 0:
        return response_data['candidates'][0]['content']['parts'][0]['text']
    else:
        return "Error analyzing resume. Please try again."

# Custom CSS for dark theme
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stButton>button {
        background-color: #00FF9D;
        color: #000000;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
        border: none;
        box-shadow: 0 0 10px #00FF9D;
    }
    .stButton>button:hover {
        background-color: #00CC7D;
        box-shadow: 0 0 15px #00FF9D;
    }
    .result-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        background-color: #1E1E1E;
        border: 1px solid #333333;
    }
    .score-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        border: 1px solid #00FF9D;
        box-shadow: 0 0 10px rgba(0, 255, 157, 0.2);
    }
    .decision-box {
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    .accept {
        background-color: #1E1E1E;
        color: #00FF9D;
        border: 1px solid #00FF9D;
        box-shadow: 0 0 15px rgba(0, 255, 157, 0.3);
    }
    .reject {
        background-color: #1E1E1E;
        color: #FF3131;
        border: 1px solid #FF3131;
        box-shadow: 0 0 15px rgba(255, 49, 49, 0.3);
    }
    h1, h2, h3 {
        color: #FFFFFF;
    }
    .stProgress > div > div > div {
        background-color: #00FF9D;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title("📄 Resume Scanner")
st.write("Upload your resume (PDF) to get a quick evaluation")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Show a spinner while processing
    with st.spinner("Analyzing your resume..."):
        # Extract text from PDF
        resume_text = extract_text_from_pdf(uploaded_file)
        
        # Analyze resume
        analysis = analyze_resume(resume_text)
        
        # Parse the analysis
        try:
            score_line = [line for line in analysis.split('\n') if 'SCORE:' in line][0]
            decision_line = [line for line in analysis.split('\n') if 'DECISION:' in line][0]
            
            score = int(score_line.split(':')[1].strip().split('/')[0])
            decision = decision_line.split(':')[1].strip()
            
            # Display results with styling
            st.markdown("### Results")
            
            # Score display
            st.markdown(f"""
            <div class="score-box">
                <h3>Score</h3>
                <h2>{score}/100</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Decision display with color
            decision_class = "accept" if decision == "ACCEPT" else "reject"
            st.markdown(f"""
            <div class="decision-box {decision_class}">
                <h3>Decision</h3>
                <h2>{decision}</h2>
            </div>
            """, unsafe_allow_html=True)
            
            # Add a progress bar for the score
            st.progress(score/100)
            
        except Exception as e:
            st.error("Error processing the results. Please try again.")
