# 🚀 Smart Resume Reviewer

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.140+-purple.svg)](https://github.com/joaomdmoura/crewAI)

A professional AI-powered backend system that analyzes resumes against job descriptions using multi-agent AI, providing detailed match scores, skill gap analysis, and generating personalized application emails.

## ✨ Features

### 🎯 **Comprehensive Analysis**
- **Match Score Calculation**: Precise percentage-based compatibility scoring
- **Skills Gap Analysis**: Identifies present and missing skills
- **Experience Evaluation**: Analyzes years of experience and education level
- **AI-Powered Recommendations**: Actionable suggestions for resume improvement

### 📧 **Professional Email Generation**
- **Personalized Content**: Tailored application emails for each job
- **Professional Formatting**: Ready-to-send email templates
- **Company-Specific**: References specific job requirements and company details

### 📊 **Advanced Features**
- **RAG-Based Matching**: Semantic similarity using vector embeddings
- **Multi-Agent Analysis**: Specialized AI agents for different analysis aspects
- **PDF Report Generation**: Professional downloadable reports
- **Modern Web Interface**: Responsive, user-friendly design

### 🔧 **Technical Capabilities**
- **PDF Processing**: Extract text from resume PDFs
- **Natural Language Processing**: Advanced text analysis and understanding
- **Vector Similarity**: Semantic matching using sentence transformers
- **Real-time Processing**: Live progress tracking during analysis

## 🛠 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package installer)
- Git

### 1. Clone the Repository
```bash
git clone https://github.com/amaarkhan/Smart-Resume-Reviewer.git
cd Smart-Resume-Reviewer/resume_reviewer
```

### 2. Create Virtual Environment
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies
```bash
# Using pip
pip install -e .

# Or using uv (recommended)
pip install uv
uv sync
```

### 4. Environment Configuration
Create a `.env` file in the `resume_reviewer` directory:
```env
MODEL=gemini/gemini-1.5-flash
GEMINI_API_KEY=your_gemini_api_key_here
```

**Get your Gemini API key:**
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create a new API key
3. Copy and paste it into your `.env` file

## 🚀 Usage

### Command Line Interface
```bash
# Basic analysis
python -m resume_reviewer.main

# Training mode
python -m resume_reviewer.main train <iterations> <filename>

# Test mode
python -m resume_reviewer.main test <iterations> <eval_llm>
```

## 📱 Web Interface Guide

### 1. **Upload Documents**
- Navigate to the Upload page
- Select your resume (PDF format)
- Paste the complete job description
- Click "Analyze Resume"

### 2. **View Analysis Progress**
- Monitor real-time progress through 4 stages:
  - Resume Parsing
  - Job Analysis
  - Skills Matching
  - Email Generation

### 3. **Review Results**
- **Match Score**: Visual percentage with color-coded rating
- **Skills Analysis**: Present vs missing skills comparison
- **Experience Profile**: Years of experience and education level
- **AI Recommendations**: Specific improvement suggestions
- **Generated Email**: Professional, ready-to-send application email

### 4. **Download & Share**
- Download comprehensive PDF reports
- Copy email to clipboard
- Share results with others

## 🏗 Project Structure

```
resume_reviewer/
├── src/resume_reviewer/
│   ├── crew.py               # CrewAI agent definitions
│   ├── main.py               # CLI entry point
│   ├── pdf_reader.py         # PDF text extraction
│   ├── config/
│   │   ├── agents.yaml       # AI agent configurations
│   │   └── tasks.yaml        # Task definitions
│   ├── rag/
│   │   ├── embedder.py       # Text embedding utilities
│   │   ├── matcher.py        # Resume-job matching logic
│   │   └── vector_db.py      # Vector database operations
│   └── tools/               # Custom CrewAI tools
├── documents/               # Sample documents
├── uploads/                # Uploaded resumes
├── reports/               # Generated reports
└── pyproject.toml         # Project configuration
```

## 🤖 AI Agents

The system uses 4 specialized AI agents:

1. **Resume Parsing Specialist**: Extracts skills, experience, and qualifications
2. **Job Description Analyzer**: Identifies requirements and responsibilities
3. **Resume-to-Job Matching Agent**: Calculates compatibility and generates recommendations
4. **Application Email Writer**: Creates personalized, professional emails

## 🔧 Configuration

### Environment Variables
- `MODEL`: AI model to use (default: gemini/gemini-1.5-flash)
- `GEMINI_API_KEY`: Your Google Gemini API key

### Customization
- Modify `config/agents.yaml` to adjust AI agent behavior
- Update `config/tasks.yaml` to change analysis tasks
- `GET /upload`: Upload interface
- `GET /analyze`: Analysis progress page
- `GET /history`: Analysis history

## 🛡 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
# Reinstall dependencies
pip install -e .
```

**2. API Key Issues**
```bash
# Check your .env file
cat .env
# Ensure GEMINI_API_KEY is set correctly
```

**3. PDF Processing Errors**
```bash
# Install PyMuPDF separately
pip install PyMuPDF
```

**4. Port Already in Use**
```bash
## 📈 Performance Tips

- **File Size**: Keep resume PDFs under 16MB
- **Job Descriptions**: Include complete, detailed job postings
- **Skills**: Use standard technology and skill names
- **Internet**: Ensure stable connection for AI analysis

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Sentence Transformers](https://www.sbert.net/) for text embeddings
- [FAISS](https://faiss.ai/) for vector similarity search

## 📞 Support

For support, email info@smartresumerviewer.com or create an issue on GitHub.

---

**Made with ❤️ by the Smart Resume Reviewer Team**