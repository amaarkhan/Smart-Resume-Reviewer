#!/usr/bin/env python
import sys
import warnings
from datetime import datetime

from resume_reviewer.crew import ResumeReviewer
from resume_reviewer.pdf_reader import extract_text_from_pdf
from resume_reviewer.report_formatter import formatter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew with professional output formatting.
    """
    # Extract texts
    resume_text = extract_text_from_pdf("documents/Amaarkhan.pdf")
    job_text = open("documents/job.txt").read()
    
    inputs = {
        'resume_text': resume_text,
        'job_description': job_text,
        'current_year': str(datetime.now().year)
    }
    
    try:
        # Run the crew analysis
        print("🚀 Starting Smart Resume Reviewer Analysis...")
        print("=" * 70)
        
        result = ResumeReviewer().crew().kickoff(inputs=inputs)
        
        print("\n" + "=" * 70)
        print("✅ Analysis completed successfully!")
        print("📧 Professional email has been generated and saved to email.md")
        
        # Extract and clean up the email
        try:
            with open("email.md", "r", encoding="utf-8") as f:
                email_content = f.read()
            
            # Format email professionally and remove placeholders
            clean_email = formatter.format_email_professionally(
                email_content, resume_text, job_text
            )
            
            # Save the cleaned email
            with open("email.md", "w", encoding="utf-8") as f:
                f.write(clean_email)
            
            print("📧 Email has been cleaned and formatted professionally!")
            
        except Exception as e:
            print(f"⚠️ Warning: Could not process email file: {e}")
        
        print("=" * 70)
        
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'resume_text': extract_text_from_pdf("documents/Amaarkhan.pdf"),
        'job_description': open("documents/job.txt").read(),
        'current_year': str(datetime.now().year)
    }

    try:
        ResumeReviewer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        ResumeReviewer().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and return the results.
    """
    inputs = {
        'resume_text': extract_text_from_pdf("documents/resume.pdf"),  # ✅ fixed
        'job_description': open("documents/job.txt").read(),
        'current_year': str(datetime.now().year)
    }

    try:
        ResumeReviewer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
