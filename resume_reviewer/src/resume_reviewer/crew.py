from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from resume_reviewer.tools.custom_tool import RAGMatchTool

@CrewBase
class ResumeReviewer():
    """ResumeReviewer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def resume_extractor(self) -> Agent:
        return Agent(config=self.agents_config['resume_extractor'], verbose=True)

    @agent
    def job_extractor(self) -> Agent:
        return Agent(config=self.agents_config['job_extractor'], verbose=True)

    @agent
    def matchmaker(self) -> Agent:
        return Agent(config=self.agents_config['matchmaker'], tools=[RAGMatchTool()], verbose=True)

    @agent
    def email_writer(self) -> Agent:
        return Agent(config=self.agents_config['email_writer'], verbose=True)

    @task
    def parse_resume_task(self) -> Task:
        return Task(config=self.tasks_config['parse_resume_task'])

    @task
    def parse_job_task(self) -> Task:
        return Task(config=self.tasks_config['parse_job_task'])

    @task
    def match_task(self) -> Task:
        return Task(config=self.tasks_config['match_task'])

    @task
    def email_task(self) -> Task:
        return Task(config=self.tasks_config['email_task'], output_file='email.md')

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Order matters
            verbose=True
        )

