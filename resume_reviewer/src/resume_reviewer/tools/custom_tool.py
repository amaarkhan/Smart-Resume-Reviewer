from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from resume_reviewer.rag.matcher import compare_resume_to_job
from resume_reviewer.report_formatter import formatter


class RAGMatchToolInput(BaseModel):
    """Input schema for RAG Match Tool."""
    resume_text: str = Field(..., description="The resume text to analyze.")
    job_text: str = Field(..., description="The job description text to match against.")


class RAGMatchTool(BaseTool):
    name: str = "RAG Resume Matcher"
    description: str = (
        "Compare resume to job description using semantic search and return professional analysis with tables and formatting."
    )
    args_schema: Type[BaseModel] = RAGMatchToolInput

    def _run(self, resume_text: str, job_text: str) -> str:
        result = compare_resume_to_job(resume_text, job_text)
        
        # Generate professional report with tables
        professional_report = formatter.generate_professional_report(
            result, resume_text, job_text
        )
        
        return professional_report


class MyCustomToolInput(BaseModel):
    """Input schema for MyCustomTool."""
    argument: str = Field(..., description="Description of the argument.")

class MyCustomTool(BaseTool):
    name: str = "Name of my tool"
    description: str = (
        "Clear description for what this tool is useful for, your agent will need this information to use it."
    )
    args_schema: Type[BaseModel] = MyCustomToolInput

    def _run(self, argument: str) -> str:
        # Implementation goes here
        return "this is an example of a tool output, ignore it and move along."
