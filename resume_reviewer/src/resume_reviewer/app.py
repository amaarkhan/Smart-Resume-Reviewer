#!/usr/bin/env python3
"""
Smart Resume Reviewer - Flask Web Application
A beautiful, modern web interface for AI-powered resume analysis and job matching.
"""

import os
import json
import threading
import time
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
from werkzeug.utils import secure_filename
import tempfile

# Import our backend components
from resume_reviewer.crew import ResumeReviewer
from resume_reviewer.pdf_reader import extract_text_from_pdf

app = Flask(__name__)
app.secret_key = 'smart-resume-reviewer-secret-key-2025'

# Configuration
UPLOAD_FOLDER = 'uploads'
REPORTS_FOLDER = 'reports'
ALLOWED_EXTENSIONS = {'pdf', 'txt', 'doc', 'docx'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['REPORTS_FOLDER'] = REPORTS_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH

# Create necessary directories
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORTS_FOLDER, exist_ok=True)

# Global analysis status storage
analysis_status = {}

def allowed_file(filename):
    """Check if file extension is allowed"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_file(file_path):
    """Extract text from uploaded file based on extension"""
    if file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    elif file_path.lower().endswith('.txt'):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        raise ValueError("Unsupported file format")

def run_analysis_in_background(session_id, resume_text, job_description):
    """Run the CrewAI analysis in a background thread"""
    try:
        # Update status
        analysis_status[session_id] = {
            'status': 'processing',
            'stage': 'Analyzing Resume...',
            'progress': 25
        }
        
        # Simulate processing stages
        time.sleep(2)
        analysis_status[session_id].update({
            'stage': 'Analyzing Job Description...',
            'progress': 50
        })
        
        time.sleep(2)
        analysis_status[session_id].update({
            'stage': 'Matching Skills...',
            'progress': 75
        })
        
        # Run the actual CrewAI analysis
        inputs = {
            'resume_text': resume_text,
            'job_description': job_description,
            'current_year': str(datetime.now().year)
        }
        
        result = ResumeReviewer().crew().kickoff(inputs=inputs)
        
        analysis_status[session_id].update({
            'stage': 'Generating Email...',
            'progress': 90
        })
        
        time.sleep(1)
        
        # Complete analysis
        analysis_status[session_id].update({
            'status': 'completed',
            'stage': 'Complete',
            'progress': 100,
            'result': {
                'resume_analysis': str(result.tasks_output[0]),
                'job_analysis': str(result.tasks_output[1]),
                'match_analysis': str(result.tasks_output[2]),
                'email': str(result.tasks_output[3]) if len(result.tasks_output) > 3 else "Email generation not available",
                'match_score': extract_match_score(str(result.tasks_output[2])),
                'matched_skills': extract_skills(str(result.tasks_output[2]), 'matched'),
                'missing_skills': extract_skills(str(result.tasks_output[2]), 'missing')
            }
        })
        
    except Exception as e:
        analysis_status[session_id] = {
            'status': 'error',
            'error': f'Analysis failed: {str(e)}'
        }

def extract_match_score(match_text):
    """Extract match percentage from analysis text"""
    import re
    match = re.search(r'(\d+(?:\.\d+)?)\s*%', match_text)
    return f"{match.group(1)}%" if match else "0%"

def extract_skills(match_text, skill_type):
    """Extract skills from analysis text"""
    # This is a simplified extraction - you might want to improve this
    if skill_type == 'matched':
        # Look for patterns indicating matched skills
        skills = []
        lines = match_text.split('\n')
        for line in lines:
            if 'matching' in line.lower() or 'present' in line.lower():
                # Extract skills from this line
                import re
                skill_matches = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', line)
                skills.extend(skill_matches[:5])  # Limit to 5 skills
        return skills[:5]
    else:
        # Look for missing/required skills
        skills = []
        lines = match_text.split('\n')
        for line in lines:
            if 'missing' in line.lower() or 'required' in line.lower() or 'needed' in line.lower():
                import re
                skill_matches = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', line)
                skills.extend(skill_matches[:5])
        return skills[:5]

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    """Upload page"""
    return render_template('upload.html')

@app.route('/api/process', methods=['POST'])
def process_files():
    """Process uploaded resume and job description"""
    try:
        # Check if files are present
        if 'resume' not in request.files:
            return jsonify({'error': 'No resume file uploaded'}), 400
        
        if 'job_description' not in request.form:
            return jsonify({'error': 'No job description provided'}), 400
        
        resume_file = request.files['resume']
        job_description = request.form['job_description']
        
        if resume_file.filename == '':
            return jsonify({'error': 'No resume file selected'}), 400
        
        if not job_description.strip():
            return jsonify({'error': 'Job description cannot be empty'}), 400
        
        if resume_file and allowed_file(resume_file.filename):
            # Generate session ID
            session_id = str(uuid.uuid4())
            
            # Save uploaded file
            filename = secure_filename(resume_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], f"{session_id}_{filename}")
            resume_file.save(file_path)
            
            # Extract text from resume
            resume_text = extract_text_from_file(file_path)
            
            # Initialize analysis status
            analysis_status[session_id] = {
                'status': 'processing',
                'stage': 'Starting Analysis...',
                'progress': 0
            }
            
            # Start background analysis
            thread = threading.Thread(
                target=run_analysis_in_background,
                args=(session_id, resume_text, job_description)
            )
            thread.daemon = True
            thread.start()
            
            return jsonify({
                'success': True,
                'session_id': session_id,
                'message': 'Analysis started successfully'
            })
        
        return jsonify({'error': 'Invalid file format. Please upload a PDF file.'}), 400
        
    except Exception as e:
        return jsonify({'error': f'Processing failed: {str(e)}'}), 500

@app.route('/analyze/<session_id>')
def analyze_page(session_id):
    """Analysis progress page"""
    if session_id not in analysis_status:
        return redirect(url_for('upload_page'))
    
    return render_template('analyze.html', session_id=session_id)

@app.route('/api/status/<session_id>')
def get_status(session_id):
    """Get analysis status"""
    if session_id not in analysis_status:
        return jsonify({'error': 'Session not found'}), 404
    
    return jsonify(analysis_status[session_id])

@app.route('/results/<session_id>')
def results_page(session_id):
    """Results page"""
    if session_id not in analysis_status:
        return redirect(url_for('upload_page'))
    
    status = analysis_status[session_id]
    if status['status'] != 'completed':
        return redirect(url_for('analyze_page', session_id=session_id))
    
    return render_template('results.html', 
                         session_id=session_id, 
                         result=status['result'])

@app.route('/api/download-report/<session_id>')
def download_report(session_id):
    """Download detailed analysis report"""
    try:
        if session_id not in analysis_status:
            return jsonify({'error': 'Session not found'}), 404
        
        status = analysis_status[session_id]
        if status['status'] != 'completed':
            return jsonify({'error': 'Analysis not completed'}), 400
        
        result = status['result']
        
        # Generate detailed report
        report_content = f"""
SMART RESUME REVIEWER - DETAILED ANALYSIS REPORT
Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Session ID: {session_id}

{'='*60}
MATCH SCORE: {result['match_score']}
{'='*60}

RESUME ANALYSIS:
{'-'*40}
{result['resume_analysis']}

JOB DESCRIPTION ANALYSIS:
{'-'*40}
{result['job_analysis']}

SKILLS MATCHING ANALYSIS:
{'-'*40}
{result['match_analysis']}

GENERATED APPLICATION EMAIL:
{'-'*40}
{result['email']}

{'='*60}
Report generated by Smart Resume Reviewer
AI-powered resume analysis and job matching system
{'='*60}
"""
        
        # Save report to file
        report_filename = f"resume_analysis_report_{session_id}.txt"
        report_path = os.path.join(app.config['REPORTS_FOLDER'], report_filename)
        
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        return send_file(report_path, as_attachment=True, 
                        download_name=f"resume_analysis_{datetime.now().strftime('%Y%m%d')}.txt")
        
    except Exception as e:
        return jsonify({'error': f'Report generation failed: {str(e)}'}), 500

def main():
    """Main entry point for the Flask application"""
    print("🚀 Starting Smart Resume Reviewer...")
    print("📊 Initializing AI analysis engine...")
    print("🌐 Web interface will be available at: http://localhost:5000")
    print("📁 Make sure to place your documents in the uploads folder")
    print("⚡ Press Ctrl+C to stop the server")
    print("-" * 60)
    
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=True)

if __name__ == '__main__':
    main()
