from crewai import Crew, Task
from agents import create_research_agent, create_summarizer_agent, create_quiz_generator_agent
from tools import web_scraper
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class EducationalTutorCrew:
    def __init__(self):
        self.research_agent = create_research_agent()
        self.summarizer_agent = create_summarizer_agent()
        self.quiz_generator_agent = create_quiz_generator_agent()

        # Set up crew
        self.crew = Crew(
            agents=[self.research_agent, self.summarizer_agent, self.quiz_generator_agent],
            tasks=[]
        )

    def process_topic(self, topic):
        """
        Process a learning topic through the agent pipeline.
        """
        # Define tasks
        research_task = Task(
            description=f"Use the web scraper tool to get educational content for the topic: {topic}. Scrape from https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}",
            agent=self.research_agent,
            tools=[web_scraper],
            expected_output="The scraped content from the educational resource."
        )

        summarize_task = Task(
            description="Summarize the crawled content into key points",
            agent=self.summarizer_agent,
            context=[research_task],
            expected_output="A concise summary of the educational content."
        )

        quiz_task = Task(
            description="Generate an interactive quiz based on the summary",
            agent=self.quiz_generator_agent,
            context=[summarize_task],
            expected_output="A quiz with questions and answers based on the content."
        )

        # Update crew tasks
        self.crew.tasks = [research_task, summarize_task, quiz_task]

        # Run the crew
        results = self.crew.kickoff()

        return {
            "resources": results[0] if len(results) > 0 else "No resources found",
            "summary": results[1] if len(results) > 1 else "No summary available",
            "quiz": results[2] if len(results) > 2 else "No quiz generated"
        }

# Global instance for use in the app
tutor_crew = EducationalTutorCrew()
