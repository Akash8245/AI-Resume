# 🎯 AI Resume Scanner

A modern, AI-powered resume screening application that uses Google's Gemini 2.0 Flash model to evaluate resumes and provide instant feedback. The application features a sleek dark theme UI with neon accents and provides quick, accurate assessments of candidate resumes.

## ✨ Features

- **AI-Powered Analysis**: Utilizes Google's Gemini 2.0 Flash model for accurate resume evaluation
- **Instant Scoring**: Provides a score from 1-100 based on resume quality
- **Clear Decision**: Gives a clear ACCEPT/REJECT recommendation
- **PDF Support**: Accepts PDF resume uploads
- **Real-time Analysis**: Quick processing and instant results

## 🚀 Live Demo

[Streamlit App Link] (Coming Soon)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/resume-scanner.git
cd resume-scanner
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run main.py
```

## 📋 Requirements

- Python 
- Streamlit
- PyPDF2
- Google Gemini API key

## 💻 Usage

1. Launch the application using `streamlit run main.py`
2. Upload a PDF resume using the file uploader
3. Wait for the AI analysis (usually takes a few seconds)
4. View the results:
   - Score (1-100)
   - ACCEPT/REJECT decision
   - Visual progress bar

## 🤖 How It Works

1. The application extracts text from the uploaded PDF resume
2. The text is sent to the Gemini 2.0 Flash model for analysis
3. The model evaluates the resume based on:
   - Content quality and relevance
   - Skills and experience
   - Education and qualifications
   - Overall presentation
4. Results are displayed with a score and clear decision

## 🙏 Reference

- Google Gemini AI for the powerful language model
- Streamlit for the amazing web framework
- PyPDF2 for PDF processing capabilities
