🎓 Educational Tutor Agent
An intelligent multi-agent system built with CrewAI that empowers users to learn effectively. It takes a topic as input, crawls educational resources, summarizes content, and generates quizzes or explanations — all in one seamless pipeline.

🚀 Features
Multi-Agent Architecture using CrewAI:
🕵️‍♂️ Research Agent: Crawls and collects educational content from the web.
🧠 Summarizer Agent: Condenses complex content into digestible key points.
❓ Quiz Generator Agent: Creates interactive quizzes based on summaries.
🌐 Integrated web scraping for real-time content retrieval.
🎨 Beautiful and responsive web interface built with Gradio.
🔁 End-to-end pipeline: From topic input to learning materials.
🔐 Secure API key management via environment variables.
🛠️ Installation
Clone the repository:




Shell
git clone https://github.com/rajsingh565/Educational_Tutor_Agent.git
cd Educational_Tutor_Agent

Create and activate a Python virtual environment (recommended):




Shell
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

Install dependencies:




Shell
pip install -r requirements.txt

Set up your OpenAI API key:

Create a .env file in the project root:



Shell
env isn’t fully supported. Syntax highlighting is based on Shell.

OPENAI_API_KEY=your_openai_api_key_here

▶️ Usage
Run the application:




Shell
python app.py

Open your browser and go to:

http://127.0.0.1:7860
Enter a learning topic (e.g., Machine Learning, World War II, Quantum Physics).

Click "Generate Learning Materials" to receive:

Summarized content
Interactive quizzes
Curated resources
🧩 Troubleshooting
✅ Ensure your internet connection is stable.
🔑 Verify your OpenAI API key is correctly set in the .env file.
🔒 For SSL certificate errors, update your system’s certificates.
🌐 If behind a proxy/firewall, configure your environment accordingly.
🤝 Contributing
Contributions are welcome! Feel free to:

Open issues
Submit pull requests
Suggest new features or improvements
