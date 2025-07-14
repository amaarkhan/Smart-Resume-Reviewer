"""
Professional report formatter for Smart Resume Reviewer
Generates clean, user-friendly output without placeholders
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any

class ProfessionalReportFormatter:
    """Formats analysis results into professional, user-friendly reports"""
    
    def __init__(self):
        self.timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        self.date_short = datetime.now().strftime("%d/%m/%Y")
    
    def extract_candidate_name(self, resume_text: str) -> str:
        """Extract candidate name from resume text"""
        # Common patterns for names at the beginning of resumes
        patterns = [
            r'^([A-Z][a-z]+ [A-Z][a-z]+)',  # First Last
            r'^([A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+)',  # First M. Last
            r'^([A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+)',  # First Middle Last
        ]
        
        lines = resume_text.strip().split('\n')[:5]  # Check first 5 lines
        
        for line in lines:
            line = line.strip()
            if len(line) > 3 and len(line) < 50:  # Reasonable name length
                for pattern in patterns:
                    match = re.search(pattern, line)
                    if match:
                        return match.group(1)
        
        return "Candidate"  # Fallback
    
    def extract_company_details(self, job_text: str) -> Dict[str, str]:
        """Extract company name and position from job description"""
        company_patterns = [
            r'Company\s*[:\-]\s*([^\n]+)',
            r'at\s+([A-Z][a-zA-Z\s&]+)(?:\s|$)',
            r'join\s+([A-Z][a-zA-Z\s&]+)',
        ]
        
        position_patterns = [
            r'Job Title\s*[:\-]\s*([^\n]+)',
            r'Position\s*[:\-]\s*([^\n]+)',
            r'Role\s*[:\-]\s*([^\n]+)',
        ]
        
        company = "this company"
        position = "this position"
        
        for pattern in company_patterns:
            match = re.search(pattern, job_text, re.IGNORECASE)
            if match:
                company = match.group(1).strip()
                break
        
        for pattern in position_patterns:
            match = re.search(pattern, job_text, re.IGNORECASE)
            if match:
                position = match.group(1).strip()
                break
        
        return {"company": company, "position": position}
    
    def format_skills_table(self, present_skills: List[str], missing_skills: List[str]) -> str:
        """Format skills analysis as a professional table"""
        table = "\n┌─────────────────────────────────────────────────────────────────┐\n"
        table += "│                        SKILLS ANALYSIS                         │\n"
        table += "├─────────────────────────────────────────────────────────────────┤\n"
        
        # Present Skills Section
        table += "│ ✅ MATCHING SKILLS                                              │\n"
        table += "├─────────────────────────────────────────────────────────────────┤\n"
        
        if present_skills:
            # Format skills in rows of 3
            for i in range(0, len(present_skills), 3):
                row_skills = present_skills[i:i+3]
                skills_text = " • ".join(row_skills)
                if len(skills_text) > 61:
                    skills_text = skills_text[:58] + "..."
                table += f"│ {skills_text:<63} │\n"
        else:
            table += "│ No matching skills found                                       │\n"
        
        # Missing Skills Section
        table += "├─────────────────────────────────────────────────────────────────┤\n"
        table += "│ ❌ SKILLS TO DEVELOP                                            │\n"
        table += "├─────────────────────────────────────────────────────────────────┤\n"
        
        if missing_skills:
            # Format missing skills in rows of 3
            for i in range(0, len(missing_skills), 3):
                row_skills = missing_skills[i:i+3]
                skills_text = " • ".join(row_skills)
                if len(skills_text) > 61:
                    skills_text = skills_text[:58] + "..."
                table += f"│ {skills_text:<63} │\n"
        else:
            table += "│ All required skills are present!                               │\n"
        
        table += "└─────────────────────────────────────────────────────────────────┘\n"
        return table
    
    def format_match_score_visual(self, score: float) -> str:
        """Create a visual representation of the match score"""
        # Determine color/symbol based on score
        if score >= 80:
            symbol = "🟢"
            rating = "EXCELLENT MATCH"
        elif score >= 65:
            symbol = "🟡"
            rating = "GOOD MATCH"
        elif score >= 45:
            symbol = "🟠"
            rating = "MODERATE MATCH"
        else:
            symbol = "🔴"
            rating = "NEEDS IMPROVEMENT"
        
        # Create progress bar
        filled = int(score / 5)  # 20 segments for 100%
        empty = 20 - filled
        progress_bar = "█" * filled + "░" * empty
        
        visual = f"\n{symbol} MATCH SCORE: {score:.1f}% - {rating}\n"
        visual += f"[{progress_bar}] {score:.1f}%\n"
        
        return visual
    
    def remove_placeholders(self, email_content: str, candidate_name: str, company: str, position: str) -> str:
        """Remove all placeholders from email and make it ready to send"""
        cleaned_email = email_content
        
        # Remove common placeholders and instructional text
        patterns_to_remove = [
            r'\[Your Name\]',
            r'\[Your Phone Number\]',
            r'\[Your Email Address\]',
            r'\[Candidate Name\]',
            r'\[Hiring Manager Name\]',
            r'\[Hiring Manager/Recruiter Name\]',
            r'\[Position\]',
            r'\[Platform where.*?\]\.?',
            r'\[Mention something specific.*?\]\.?',
            r'\[Key Qualification\]',
            r'\[mention a specific project.*?\]\.?',
            r'\[Actual Position Title\]',
            r'\[Actual Company Name\]',
            r'\[Actual Candidate Name\]',
            r'as advertised on \[Platform where.*?\]\.?',
            r'Axiom World\'s commitment to \[Mention something.*?\]',
            r', as advertised on \[Platform.*?\]',
            r'\.  \[Mention something.*?\]',
            r', \[mention.*?\]',
            r'- If this information is not available, remove this part of the sentence\.',
            r'otherwise remove this clause',
            r'if known from research, otherwise remove this clause',
        ]
        
        # Replace specific placeholders with actual content first
        cleaned_email = re.sub(r'\[Candidate Name\]', candidate_name, cleaned_email, flags=re.IGNORECASE)
        cleaned_email = re.sub(r'\[Position\]', position, cleaned_email, flags=re.IGNORECASE)
        cleaned_email = re.sub(r'\[Actual Position Title\]', position, cleaned_email, flags=re.IGNORECASE)
        cleaned_email = re.sub(r'\[Actual Company Name\]', company, cleaned_email, flags=re.IGNORECASE)
        cleaned_email = re.sub(r'\[Actual Candidate Name\]', candidate_name, cleaned_email, flags=re.IGNORECASE)
        
        # Remove all remaining patterns
        for pattern in patterns_to_remove:
            cleaned_email = re.sub(pattern, '', cleaned_email, flags=re.IGNORECASE)
        
        # Clean up formatting issues caused by removal
        cleaned_email = re.sub(r'\s+', ' ', cleaned_email)  # Multiple spaces
        cleaned_email = re.sub(r'\n\s*\n', '\n\n', cleaned_email)  # Multiple newlines
        cleaned_email = re.sub(r',\s*,', ',', cleaned_email)  # Double commas
        cleaned_email = re.sub(r'\.\s*\.', '.', cleaned_email)  # Double periods
        cleaned_email = re.sub(r',\s*\.', '.', cleaned_email)  # Comma before period
        cleaned_email = re.sub(r'\.\s*,', ',', cleaned_email)  # Period before comma
        cleaned_email = re.sub(r'\s+\.', '.', cleaned_email)  # Space before period
        cleaned_email = re.sub(r'\s+,', ',', cleaned_email)  # Space before comma
        
        # Fix sentence structure issues
        cleaned_email = re.sub(r'(\w)\s+strongly resonates', r'\1 strongly resonates', cleaned_email)
        cleaned_email = re.sub(r'at\s+\.', '.', cleaned_email)
        cleaned_email = re.sub(r'at\s+,', ',', cleaned_email)
        
        # Ensure proper formatting
        cleaned_email = cleaned_email.strip()
        
        return cleaned_email
    
    def generate_professional_report(self, analysis_result: Dict[str, Any], 
                                   resume_text: str, job_text: str) -> str:
        """Generate a comprehensive, professional report"""
        
        candidate_name = self.extract_candidate_name(resume_text)
        company_details = self.extract_company_details(job_text)
        
        # Extract analysis data
        match_score = analysis_result.get('numeric_score', 0)
        present_skills = analysis_result.get('present_skills', [])
        missing_skills = analysis_result.get('missing_skills', [])
        recommendations = analysis_result.get('recommendations', '')
        experience_years = analysis_result.get('experience_years', 0)
        education_level = analysis_result.get('education_level', 'Unknown').upper()
        
        # Build the report
        report = f"""
╔═══════════════════════════════════════════════════════════════════╗
║                   SMART RESUME REVIEWER REPORT                   ║
║                      Generated on {self.date_short}                      ║
╚═══════════════════════════════════════════════════════════════════╝

👤 CANDIDATE: {candidate_name}
🏢 POSITION: {company_details['position']} at {company_details['company']}
📅 ANALYSIS DATE: {self.timestamp}

{self.format_match_score_visual(match_score)}

{self.format_skills_table(present_skills, missing_skills)}

┌─────────────────────────────────────────────────────────────────┐
│                       CANDIDATE PROFILE                        │
├─────────────────────────────────────────────────────────────────┤
│ Experience Level: {experience_years} years                                    │
│ Education: {education_level:<15}                                │
│ Skills Count: {len(present_skills)} matching, {len(missing_skills)} to develop                     │
└─────────────────────────────────────────────────────────────────┘

📋 PROFESSIONAL RECOMMENDATIONS:
{recommendations}

═══════════════════════════════════════════════════════════════════
Report generated by Smart Resume Reviewer AI • Powered by CrewAI
"""
        
        return report
    
    def format_email_professionally(self, email_content: str, resume_text: str, job_text: str) -> str:
        """Format email professionally without placeholders"""
        
        candidate_name = self.extract_candidate_name(resume_text)
        company_details = self.extract_company_details(job_text)
        
        # Remove placeholders and clean up
        clean_email = self.remove_placeholders(
            email_content, 
            candidate_name, 
            company_details['company'], 
            company_details['position']
        )
        
        # Ensure professional structure
        if not clean_email.startswith('Subject:'):
            subject = f"Subject: Application for {company_details['position']} Position - {candidate_name}"
            clean_email = f"{subject}\n\n{clean_email}"
        
        # Remove duplicate "Best regards" sections
        clean_email = re.sub(r'Best regards,\s*\n*\s*Candidate\s*$', '', clean_email)
        clean_email = re.sub(r'Best regards,\s*\n*\s*Best regards,', 'Best regards,', clean_email)
        
        # Add proper line breaks for professional formatting
        clean_email = re.sub(r'(Subject: [^\n]+)', r'\1\n', clean_email)
        clean_email = re.sub(r'(Dear [^,]+,)', r'\1\n\n', clean_email)
        clean_email = re.sub(r'(Best regards,)', r'\n\n\1', clean_email)
        
        # Ensure candidate name is in closing if missing
        if candidate_name not in clean_email[-200:]:  # If name not in closing
            if not clean_email.endswith('\n'):
                clean_email += '\n'
            clean_email += f"\nBest regards,\n{candidate_name}"
        
        # Clean up extra spaces and newlines
        clean_email = re.sub(r'\n{3,}', '\n\n', clean_email)  # Max 2 newlines
        clean_email = clean_email.strip()
        
        return clean_email

# Global formatter instance
formatter = ProfessionalReportFormatter()
