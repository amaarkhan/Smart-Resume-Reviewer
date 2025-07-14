"""
Enhanced resume-job matching with comprehensive analysis
"""
from .vector_db import build_vector_db
from .embedder import get_embedder, ResumeEmbedder
import re
from typing import Dict, List, Tuple
import numpy as np

class AdvancedMatcher:
    """Advanced matching engine for resume-job analysis"""
    
    def __init__(self):
        self.embedder = ResumeEmbedder()
    
    def extract_skills_from_text(self, text: str) -> List[str]:
        """Extract skills and technologies from text"""
        # Common technology and skill keywords
        skill_patterns = [
            # Programming languages
            r'\b(?:python|java|javascript|typescript|c\+\+|c#|go|rust|php|ruby|swift|kotlin|scala)\b',
            # Web technologies
            r'\b(?:html|css|react|angular|vue|node\.js|express|django|flask|spring|laravel)\b',
            # Databases
            r'\b(?:mysql|postgresql|mongodb|redis|elasticsearch|oracle|sql server)\b',
            # Cloud & DevOps
            r'\b(?:aws|azure|gcp|docker|kubernetes|jenkins|terraform|ansible)\b',
            # Tools & Frameworks
            r'\b(?:git|github|gitlab|jira|confluence|figma|photoshop|illustrator)\b',
        ]
        
        skills = set()
        text_lower = text.lower()
        
        for pattern in skill_patterns:
            matches = re.findall(pattern, text_lower, re.IGNORECASE)
            skills.update(matches)
        
        # Also extract from skills sections
        skills_section = self.embedder.extract_skills_section(text)
        skills.update([skill.lower() for skill in skills_section])
        
        return list(skills)
    
    def calculate_experience_years(self, text: str) -> int:
        """Extract years of experience from text"""
        # Look for patterns like "5 years", "3+ years", etc.
        patterns = [
            r'(\d+)\+?\s*years?\s*(?:of\s*)?experience',
            r'(\d+)\+?\s*years?\s*in',
            r'experience\s*[:\-]\s*(\d+)\+?\s*years?',
        ]
        
        years = []
        for pattern in patterns:
            matches = re.findall(pattern, text.lower())
            years.extend([int(match) for match in matches])
        
        return max(years) if years else 0
    
    def extract_education_level(self, text: str) -> str:
        """Extract education level from text"""
        education_patterns = {
            'phd': r'\b(?:phd|ph\.d|doctorate|doctoral)\b',
            'masters': r'\b(?:masters?|m\.s|m\.a|mba|master of)\b',
            'bachelors': r'\b(?:bachelors?|b\.s|b\.a|bachelor of)\b',
            'associate': r'\b(?:associate|a\.s|a\.a)\b',
        }
        
        text_lower = text.lower()
        for level, pattern in education_patterns.items():
            if re.search(pattern, text_lower):
                return level
        
        return 'unknown'
    
    def calculate_match_score(self, resume_skills: List[str], job_skills: List[str]) -> float:
        """Calculate match percentage between resume and job skills"""
        if not job_skills:
            return 0.0
        
        resume_set = set(skill.lower().strip() for skill in resume_skills)
        job_set = set(skill.lower().strip() for skill in job_skills)
        
        intersection = resume_set.intersection(job_set)
        union = resume_set.union(job_set)
        
        if not union:
            return 0.0
        
        # Calculate Jaccard similarity
        jaccard = len(intersection) / len(job_set)
        return min(jaccard * 100, 100.0)  # Cap at 100%
    
    def identify_missing_skills(self, resume_skills: List[str], job_skills: List[str]) -> List[str]:
        """Identify skills mentioned in job but missing from resume"""
        resume_set = set(skill.lower().strip() for skill in resume_skills)
        job_set = set(skill.lower().strip() for skill in job_skills)
        
        missing = job_set - resume_set
        return list(missing)
    
    def generate_recommendations(self, missing_skills: List[str], match_score: float) -> str:
        """Generate improvement recommendations"""
        recommendations = []
        
        if match_score < 50:
            recommendations.append("Your resume shows a low match with this position.")
        elif match_score < 75:
            recommendations.append("Your resume shows a moderate match with this position.")
        else:
            recommendations.append("Your resume shows a strong match with this position!")
        
        if missing_skills:
            if len(missing_skills) <= 3:
                recommendations.append(f"Consider highlighting or developing these skills: {', '.join(missing_skills[:3])}")
            else:
                recommendations.append(f"Focus on developing key skills like: {', '.join(missing_skills[:3])} and {len(missing_skills)-3} others")
        
        if match_score < 75:
            recommendations.append("Consider tailoring your resume to better highlight relevant experience for this role.")
        
        return ". ".join(recommendations) + "."

def compare_resume_to_job(resume_text: str, job_text: str) -> dict:
    """Enhanced resume-job comparison with detailed analysis"""
    matcher = AdvancedMatcher()
    
    # Clean text
    resume_clean = matcher.embedder.preprocess_text(resume_text)
    job_clean = matcher.embedder.preprocess_text(job_text)
    
    # Extract skills
    resume_skills = matcher.extract_skills_from_text(resume_clean)
    job_skills = matcher.extract_skills_from_text(job_clean)
    
    # Calculate match score
    match_score = matcher.calculate_match_score(resume_skills, job_skills)
    
    # Identify missing skills
    missing_skills = matcher.identify_missing_skills(resume_skills, job_skills)
    
    # Generate recommendations
    recommendations = matcher.generate_recommendations(missing_skills, match_score)
    
    # Extract additional info
    experience_years = matcher.calculate_experience_years(resume_clean)
    education_level = matcher.extract_education_level(resume_clean)
    
    # Use vector similarity for semantic matching
    try:
        vector_store = build_vector_db([job_text])
        similar_docs = vector_store.similarity_search(query=resume_text, k=1)
        semantic_match = similar_docs[0].page_content if similar_docs else "No semantic match found"
    except Exception:
        semantic_match = "Semantic analysis unavailable"
    
    return {
        "match_score": f"{match_score:.1f}%",
        "numeric_score": match_score,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
        "missing_skills": missing_skills,
        "present_skills": list(set(resume_skills).intersection(set(job_skills))),
        "recommendations": recommendations,
        "experience_years": experience_years,
        "education_level": education_level,
        "retrieved_section": semantic_match[:500] + "..." if len(semantic_match) > 500 else semantic_match
    }
