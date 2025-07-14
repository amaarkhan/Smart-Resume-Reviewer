# Smart Resume Reviewer 🚀

A professional AI-powered resume analysis and job matching backend using CrewAI.

## Features 📊

✅ **Resume Analysis**: Process PDF or text resumes for comprehensive analysis  
✅ **Job Matching**: Compare resumes against job descriptions using AI agents  
✅ **Skills Assessment**: Identify matching and missing skills with visual tables  
✅ **Match Scoring**: Get percentage-based compatibility scores with progress bars  
✅ **Professional Reports**: Generate detailed analysis reports with clean formatting  
✅ **Email Templates**: Generate ready-to-send application emails without placeholders  
✅ **Command Line Interface**: Easy-to-use CLI for automation  

## ✨ New Professional Features

🎯 **Visual Match Scoring**: Color-coded progress bars with ratings (Excellent/Good/Moderate/Needs Improvement)  
📊 **Skills Analysis Tables**: Professional formatted tables showing matching vs missing skills  
📧 **Placeholder-Free Emails**: Fully completed emails ready to send without [Your Name] placeholders  
🎨 **Clean Formatting**: User-friendly output with tables, visual elements, and clear structure  

## Quick Start 🌟

### Basic Usage
```powershell
cd resume_reviewer
uv run run_crew
```

### Testing Backend
```powershell
cd resume_reviewer  
python test_backend.py
```

### Training Mode
```powershell
cd resume_reviewer  
uv run train <iterations> <filename>
```

### Test Mode  
```powershell
cd resume_reviewer
uv run test
```

## How to Use 📋

1. **Place Files**: Put your resume (PDF) and job description (TXT) in the `documents/` folder
2. **Run Analysis**: Execute `uv run run_crew` to start the AI-powered analysis
3. **Review Results**: The system will output detailed analysis results with professional formatting
4. **Get Professional Email**: Receive a ready-to-send email without any placeholders

## Sample Output 📄

### Professional Match Score
```
🟢 MATCH SCORE: 75.2% - GOOD MATCH
[████████████████░░░░] 75.2%
```

### Skills Analysis Table
```
┌─────────────────────────────────────────────────────────────────┐
│                        SKILLS ANALYSIS                         │
├─────────────────────────────────────────────────────────────────┤
│ ✅ MATCHING SKILLS                                              │
│ react • css • javascript • html • java                         │
├─────────────────────────────────────────────────────────────────┤
│ ❌ SKILLS TO DEVELOP                                            │
│ angular • vue • typescript • node.js                           │
└─────────────────────────────────────────────────────────────────┘
```

### Professional Email (No Placeholders!)
```
Subject: Application for Front-end Developer - John Smith

Dear Hiring Manager,

I am writing to express my strong interest in the Front-end Developer 
position at TechCorp. My background in React, CSS, and JavaScript 
aligns perfectly with your requirements...

Best regards,
John Smith
```

## Features Breakdown 🔍

### Match Score
- **80%+**: 🟢 Excellent match - highly qualified
- **65-79%**: 🟡 Good match with minor gaps
- **45-64%**: 🟠 Moderate match - skill development needed
- **<45%**: 🔴 Significant gaps requiring development

### Skills Analysis
- **✅ Matching Skills**: Skills found in both resume and job description
- **❌ Missing Skills**: Required skills not found in resume
- **Development Recommendations**: Prioritized list of skills to learn

### Professional Email
- Auto-extracted candidate name from resume
- Auto-extracted company name and position from job description
- NO placeholders - everything filled in automatically
- Professional formatting and language
- Ready to copy and send immediately

## File Structure 📁

```
resume_reviewer/
├── src/resume_reviewer/
│   ├── main.py                # CLI entry point with professional output
│   ├── crew.py                # CrewAI agent definitions
│   ├── pdf_reader.py          # PDF text extraction
│   ├── report_formatter.py    # Professional report formatting
│   ├── config/
│   │   ├── agents.yaml        # AI agent configurations
│   │   └── tasks.yaml         # Task definitions with professional output
│   ├── rag/
│   │   ├── embedder.py        # Text embedding utilities
│   │   ├── matcher.py         # Resume-job matching logic
│   │   └── vector_db.py       # Vector database operations
│   └── tools/                 # Custom CrewAI tools with formatting
├── documents/                 # Sample documents
├── test_backend.py           # Backend testing script
└── pyproject.toml            # Project configuration
```

## Professional Output Examples 📋

The system now generates:

1. **Visual Progress Bars**: Clear percentage indicators with color coding
2. **Formatted Tables**: Professional skills analysis in table format
3. **Clean Reports**: Structured output with headers, sections, and visual elements
4. **Complete Emails**: No placeholders, ready-to-send professional emails
5. **User-Friendly Language**: Clear, actionable recommendations without technical jargon

## Requirements 💻

- Python 3.10+
- CrewAI (AI agents)
- PyMuPDF (PDF processing)
- Sentence Transformers (semantic matching)
- FAISS (vector search)
- LangChain (text processing)

## Troubleshooting 🔧

### "No matching skills found"
1. Ensure skills are clearly listed in resume
2. Use common technology names (react, python, css)
3. Include skills in dedicated "Skills" section

### PDF extraction issues
1. Ensure file is a valid PDF
2. Check file size and format
3. Try converting to text format as fallback

### Email contains placeholders
This should no longer happen! The system automatically extracts:
- Candidate name from resume
- Company name from job description
- Position title from job posting

## Development 🛠️

### Adding New Features
1. Edit report formatting in `report_formatter.py`
2. Update task outputs in `config/tasks.yaml`
3. Modify agent behavior in `config/agents.yaml`

### Testing
```powershell
# Test complete backend
python test_backend.py

# Test with your files
# 1. Place resume.pdf and job.txt in documents/
# 2. Run: uv run run_crew
```

## Version History 📈

- **v1.0**: Basic resume parsing and matching
- **v1.1**: Added professional table formatting
- **v1.2**: Removed all placeholders from emails
- **v1.3**: Added visual progress bars and color coding
- **v1.4**: Professional report generation with clean layout

---

**Smart Resume Reviewer** - Professional AI-powered resume analysis without the fluff! 🎯
