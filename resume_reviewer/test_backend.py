#!/usr/bin/env python
"""
Simple test script to verify the Smart Resume Reviewer backend works correctly
"""

import os
import sys
from datetime import datetime

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from resume_reviewer.crew import ResumeReviewer
from resume_reviewer.pdf_reader import extract_text_from_pdf
from resume_reviewer.report_formatter import formatter
from resume_reviewer.rag.matcher import compare_resume_to_job

def test_resume_analysis():
    """Test the complete resume analysis pipeline"""
    
    print("🧪 Testing Smart Resume Reviewer Backend...")
    print("=" * 60)
    
    # Check if required files exist
    resume_path = "documents/Amaarkhan.pdf"
    job_path = "documents/job.txt"
    
    if not os.path.exists(resume_path):
        print(f"❌ Resume file not found: {resume_path}")
        return False
    
    if not os.path.exists(job_path):
        print(f"❌ Job description file not found: {job_path}")
        return False
    
    try:
        # Test PDF extraction
        print("📄 Testing PDF extraction...")
        resume_text = extract_text_from_pdf(resume_path)
        print(f"✅ Extracted {len(resume_text)} characters from resume")
        
        # Test job description reading
        print("📋 Reading job description...")
        with open(job_path, 'r', encoding='utf-8') as f:
            job_text = f.read()
        print(f"✅ Read {len(job_text)} characters from job description")
        
        # Test RAG matching
        print("🔍 Testing RAG matching...")
        match_result = compare_resume_to_job(resume_text, job_text)
        print(f"✅ Match score: {match_result.get('match_score', 'N/A')}")
        
        # Test report formatting
        print("📊 Testing report formatting...")
        professional_report = formatter.generate_professional_report(
            match_result, resume_text, job_text
        )
        print("✅ Professional report generated successfully")
        
        # Test email formatting
        print("📧 Testing email formatting...")
        sample_email = """Subject: Application for Front end Intern Position

Dear Hiring Manager,

I am writing to express my interest in the Front end Intern position at your company.

Best regards,
[Your Name]"""
        
        clean_email = formatter.format_email_professionally(
            sample_email, resume_text, job_text
        )
        print("✅ Email formatting successful")
        
        print("\n" + "=" * 60)
        print("🎉 All backend tests passed!")
        print("✅ The Smart Resume Reviewer backend is working correctly.")
        
        # Save test results
        with open("test_results.txt", "w", encoding="utf-8") as f:
            f.write("SMART RESUME REVIEWER - TEST RESULTS\n")
            f.write("=" * 50 + "\n")
            f.write(f"Test Date: {datetime.now()}\n\n")
            f.write("PROFESSIONAL REPORT SAMPLE:\n")
            f.write("-" * 30 + "\n")
            f.write(professional_report[:1000] + "...\n\n")
            f.write("CLEAN EMAIL SAMPLE:\n")
            f.write("-" * 20 + "\n")
            f.write(clean_email[:500] + "...")
        
        print("📝 Test results saved to test_results.txt")
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == "__main__":
    success = test_resume_analysis()
    sys.exit(0 if success else 1)
