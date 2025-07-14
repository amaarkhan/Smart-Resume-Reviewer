"""
Enhanced embedder module for converting text to vector embeddings
"""
from langchain_community.embeddings import SentenceTransformerEmbeddings
from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List, Union
import re

class ResumeEmbedder:
    """Enhanced embedder for resume and job description matching"""
    
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.langchain_embedder = SentenceTransformerEmbeddings(model_name=model_name)
    
    def embed_text(self, text: Union[str, List[str]]) -> np.ndarray:
        """Convert text to embeddings"""
        if isinstance(text, str):
            text = [text]
        return self.model.encode(text, convert_to_tensor=False)
    
    def preprocess_text(self, text: str) -> str:
        """Clean and preprocess text for better embedding"""
        # Remove extra whitespace and normalize
        text = re.sub(r'\s+', ' ', text.strip())
        # Remove special characters but keep meaningful punctuation
        text = re.sub(r'[^\w\s\.\,\-\(\)]', ' ', text)
        return text
    
    def extract_skills_section(self, text: str) -> List[str]:
        """Extract skills from text using patterns"""
        skills = []
        # Common skill patterns
        patterns = [
            r'(?i)skills?[:\-]?\s*([^\n]+)',
            r'(?i)technologies?[:\-]?\s*([^\n]+)',
            r'(?i)programming languages?[:\-]?\s*([^\n]+)',
            r'(?i)tools?[:\-]?\s*([^\n]+)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text)
            for match in matches:
                # Split by common separators
                skill_items = re.split(r'[,;|]', match)
                skills.extend([skill.strip() for skill in skill_items if skill.strip()])
        
        return list(set(skills))  # Remove duplicates

def get_embedder():
    """Get the LangChain embedder for compatibility"""
    return SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
