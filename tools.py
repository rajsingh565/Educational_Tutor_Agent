import requests
from bs4 import BeautifulSoup
from crewai.tools import tool

@tool("Web Scraper Tool")
def web_scraper(url: str) -> str:
    """
    Scrapes text content from a given URL for educational resources.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract text content
        text = soup.get_text(separator=' ', strip=True)
        return text[:2000]  # Limit to 2000 chars for demo
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"

# Additional tools can be added here as needed
