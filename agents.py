from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4", api_key=os.getenv("OPENAI_API_KEY"))

def create_research_agent():
    return Agent(
        role="Research Agent",
        goal="Find and crawl educational resources for given topics",
        backstory="You are an expert researcher who specializes in finding high-quality educational content from the web.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

def create_summarizer_agent():
    return Agent(
        role="Summarizer Agent",
        goal="Summarize educational content into concise and understandable formats",
        backstory="You are a skilled summarizer who condenses complex information into key points.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )

def create_quiz_generator_agent():
    return Agent(
        role="Quiz Generator Agent",
        goal="Generate interactive quizzes and explanations based on summarized content",
        backstory="You are a quiz master who creates engaging questions to test knowledge and provide explanations.",
        llm=llm,
        allow_delegation=False,
        verbose=True
    )
