# 🚀 Smart Resume Reviewer

> **Transform your job applications with AI-powered resume analysis!**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![CrewAI](https://img.shields.io/badge/CrewAI-0.140+-purple.svg)](https://github.com/joaomdmoura/crewAI)

**Smart Resume Reviewer** is an intelligent AI system that analyzes your resume against job descriptions, giving you instant feedback on how well you match the role. Get detailed insights, skill gap analysis, and even generate professional application emails - all powered by advanced AI agents.

## 📸 See It In Action

### Real-Time Analysis Progress
![Analysis Progress](assets/analysis-progress.png)
*Watch as AI agents analyze your resume step by step*

### Comprehensive Results Dashboard  
![Results Dashboard](assets/results-dashboard.png)
*Get detailed match scores, skills analysis, and professional recommendations*

## ✨ What Can It Do For You?

### 🎯 **Get Instant Match Scores**
- See exactly how well your resume matches any job (percentage score)
- Visual progress bars with color-coded ratings
- Understand your competitive advantage

### 🔍 **Discover Skill Gaps**
- Find out which skills you already have that match the job
- Identify missing skills you need to develop
- Get prioritized learning recommendations

### 📧 **Generate Professional Emails**
- Automatically create personalized application emails
- No more generic cover letters
- Ready-to-send, professionally formatted messages

### 🚀 **Advanced AI Analysis**
- 4 specialized AI agents working together
- Semantic understanding of your experience
- Real-time processing with live updates

## 🎬 How It Works (Super Simple!)

### Step 1: Upload Your Resume
Just drag and drop your PDF resume - that's it!

### Step 2: Paste the Job Description  
Copy the job posting and paste it in the text box

### Step 3: Watch the Magic Happen
Our AI agents analyze everything in real-time:
- 🤖 **Resume Parser** extracts your skills and experience
- 🎯 **Job Analyzer** understands what the employer wants  
- 🔗 **Matcher** compares and scores the fit
- ✍️ **Email Writer** creates your application email

### Step 4: Get Your Results
- **Match Score**: Clear percentage showing how well you fit
- **Skills Analysis**: What you have vs what you need
- **Profile Summary**: Your experience level and education
- **Professional Email**: Ready to copy and send

## ⚡ Quick Start (5 Minutes!)

### What You Need
- Python 3.10+ installed on your computer
- A Google Gemini API key (free to get!)
- Your resume in PDF format

### Step 1: Download the Project
```bash
git clone https://github.com/amaarkhan/Smart-Resume-Reviewer.git
cd Smart-Resume-Reviewer/resume_reviewer
```

### Step 2: Get Your Free API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey) 
2. Click "Create API Key" 
3. Copy the key (keep it safe!)

### Step 3: Set Up the Environment
```bash
# Install dependencies
pip install -e .

# Create your config file
echo "GEMINI_API_KEY=your_key_here" > .env
```
*Replace `your_key_here` with the API key you copied*

### Step 4: Start the Application
```bash
# Start the web interface
uv run flask_app
```

### Step 5: Open Your Browser
Go to `http://localhost:5000` and start analyzing! 🎉

## 🎮 Using the Web Interface

### Upload Page
1. **Upload Resume**: Click to select your PDF resume
2. **Job Description**: Paste the complete job posting
3. **Analyze**: Hit the button and watch the magic happen!

### Analysis Page  
Watch in real-time as 4 AI agents work on your analysis:
- ✅ Resume analysis completed
- ✅ Job description analysis completed  
- ✅ Skills matching completed
- ✅ Email generation completed

### Results Page
Get your comprehensive analysis:
- **🎯 Match Score**: Big, clear percentage with color coding
- **📊 Skills Analysis**: What skills you have vs need
- **👤 Profile Summary**: Your experience and education level
- **📧 Application Email**: Professional, ready-to-send email

## 🛠 For Developers

### Project Structure
```
resume_reviewer/
├── src/resume_reviewer/
│   ├── app.py               # Flask web application
│   ├── crew.py              # AI agents coordination
│   ├── main.py              # Command-line interface
│   ├── config/              # AI agent configurations
│   ├── rag/                 # Resume matching logic
│   └── tools/               # Custom AI tools
├── documents/               # Sample files
├── uploads/                 # User uploads
└── reports/                 # Generated reports
```

### The AI Agents
- **Resume Parser**: Extracts skills, experience, education
- **Job Analyzer**: Understands requirements and responsibilities  
- **Matching Agent**: Calculates compatibility scores
- **Email Writer**: Generates personalized application emails

### Command Line Usage
```bash
# Analyze with CLI (backend only)
python -m resume_reviewer.main

# Train the model
python -m resume_reviewer.main train <iterations> <filename>

# Run tests
python -m resume_reviewer.main test
```

## ❓ Need Help?

### Common Issues & Solutions

**🚫 "Cannot import" errors**
```bash
pip install -e .
```

**🔑 API key not working?**
- Check your `.env` file has the correct key
- Make sure there are no extra spaces
- Try regenerating the key from Google AI Studio

**📄 PDF not reading properly?**
- Ensure your PDF is text-based (not scanned image)
- Try a different PDF or convert to text first
- Check file size is under 16MB

**🌐 Web interface not loading?**
```bash
# Try a different port
uv run flask_app --port 5001
```

### Tips for Best Results
- ✅ Use detailed, complete job descriptions
- ✅ Include all your skills in your resume
- ✅ Use standard skill names (e.g., "React" not "React.js")
- ✅ Keep resume format clean and simple

### Getting Support
- 📧 Email: info@smartresumerviewer.com
- 🐛 Report bugs: [Create GitHub Issue](https://github.com/amaarkhan/Smart-Resume-Reviewer/issues)
- 💬 Questions: Check existing issues first

## 🤝 Want to Contribute?

We'd love your help! Here's how:

1. **🍴 Fork** the repository
2. **🌟 Create** a feature branch
3. **✨ Make** your improvements  
4. **📤 Submit** a pull request

Ideas for contributions:
- 🎨 UI/UX improvements
- 🔧 New features
- 🐛 Bug fixes
- 📚 Documentation updates
- 🌐 Translations

## 📄 License & Credits

### License
MIT License - feel free to use this project however you'd like!

### Built With Love Using
- 🤖 [CrewAI](https://github.com/joaomdmoura/crewAI) - Multi-agent AI framework
- 🧠 [Sentence Transformers](https://www.sbert.net/) - Text embeddings
- ⚡ [FAISS](https://faiss.ai/) - Vector similarity search
- � [Flask](https://flask.palletsprojects.com/) - Web framework
- 🎨 Modern CSS & JavaScript for the interface

---

<div align="center">

**🚀 Ready to supercharge your job applications?**

[**Get Started Now**](https://github.com/amaarkhan/Smart-Resume-Reviewer) • [**Report Bug**](https://github.com/amaarkhan/Smart-Resume-Reviewer/issues) • [**Request Feature**](https://github.com/amaarkhan/Smart-Resume-Reviewer/issues)

**Made with ❤️ by the Smart Resume Reviewer Team**

*Star ⭐ this repo if it helped you land a job!*

</div>