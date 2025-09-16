# Educational Tutor Agent

An intelligent multi-agent system built with CrewAI that helps users learn by taking a topic as input, crawling educational resources, summarizing content, and generating quizzes or explanations.

## Features

- Multi-agent architecture using CrewAI with specialized agents:
  - Research Agent: Crawls and collects educational content from the web.
  - Summarizer Agent: Summarizes complex content into concise key points.
  - Quiz Generator Agent: Creates interactive quizzes based on summaries.
- Web scraping tool integrated for content retrieval.
- Beautiful and responsive web interface built with Gradio.
- End-to-end pipeline from topic input to learning materials.
- Environment variable support for secure API key management.

## Installation

1. Clone the repository:
   ```
   git clone <your-repo-url>
   cd Educational-Tutor-Agent
   ```

2. Create and activate a Python virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the application:
   ```
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:7860
   ```

3. Enter a learning topic in the input box (e.g., "Machine Learning", "World War II", "Quantum Physics").

4. Click "Generate Learning Materials" to get summarized content, quizzes, and resources.

## Troubleshooting

- Ensure your internet connection is stable.
- Verify your OpenAI API key is correctly set in the `.env` file.
- If you encounter SSL certificate errors, ensure your system's certificates are up to date.
- If behind a proxy or firewall, configure your environment accordingly.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## License

This project is open-source and free to use.
