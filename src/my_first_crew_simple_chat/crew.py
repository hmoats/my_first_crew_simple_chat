import os

from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class ChatInputExtractionCrewCrew:
    """ChatInputExtractionCrew crew"""

    @agent
    def chat_input_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["chat_input_specialist"],
            tools=[],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            
            max_execution_time=None,
            llm=LLM(
                model="azure/gpt-4.1",
                temperature=0.7,
            ),
            
        )
    
    @task
    def answer_user_chat_question(self) -> Task:
        import os; print("DEBUG sample_value =", os.getenv("sample_value"))
        return Task(
            config=self.tasks_config["answer_user_chat_question"],
            markdown=False,
        )


        return Task(
            expected_output="A short, factual markdown answer about the user's question.",
            markdown=True,
            human_input=True,
            inputs={
                "sample_value": {
                    "type": "string",
                    "description": "The user's question",
                    "required": True
                }
            }
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the ChatInputExtractionCrew crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            chat_llm=LLM(model="azure/gpt-4.1"),
        )


