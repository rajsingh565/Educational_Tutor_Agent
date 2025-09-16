import gradio as gr
from main import tutor_crew

def process_topic(topic):
    """
    Process the topic and return formatted results.
    """
    if not topic.strip():
        return "Please enter a valid topic.", "", ""

    results = tutor_crew.process_topic(topic)

    summary = f"## Summary\n\n{results['summary']}"
    quiz = f"## Quiz\n\n{results['quiz']}"
    resources = f"## Resources\n\n{results['resources']}"

    return summary, quiz, resources

# Custom CSS for beautiful styling
custom_css = """
.gradio-container {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

.gr-button {
    background: linear-gradient(45deg, #FE6B8B 30%, #FF8E53 90%);
    border: 0;
    border-radius: 3px;
    box-shadow: 0 3px 5px 2px rgba(255, 105, 135, .3);
    color: white;
    height: 48px;
    padding: 0 30px;
    transition: all 0.3s ease;
}

.gr-button:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 10px 2px rgba(255, 105, 135, .4);
}

.gr-textbox {
    border-radius: 8px;
    border: 2px solid #ddd;
    transition: border-color 0.3s ease;
}

.gr-textbox:focus {
    border-color: #FE6B8B;
    box-shadow: 0 0 0 2px rgba(254, 107, 139, 0.2);
}

.gr-markdown {
    background: rgba(255, 255, 255, 0.9);
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
"""

# Create the Gradio interface
with gr.Blocks(title="Educational Tutor Agent", theme=gr.themes.Soft(), css=custom_css) as iface:
    gr.Markdown("# 🎓 Educational Tutor Agent")
    gr.Markdown("Enter a topic to learn about, and get summarized content, quizzes, and more!")

    with gr.Row():
        topic_input = gr.Textbox(
            label="Learning Topic",
            placeholder="e.g., Machine Learning, World War II, Quantum Physics",
            lines=2
        )

    generate_btn = gr.Button("🚀 Generate Learning Materials", variant="primary")

    with gr.Row():
        with gr.Column():
            summary_output = gr.Markdown(label="Summary")
        with gr.Column():
            quiz_output = gr.Markdown(label="Quiz")

    resources_output = gr.Markdown(label="Resources")

    generate_btn.click(
        fn=process_topic,
        inputs=topic_input,
        outputs=[summary_output, quiz_output, resources_output]
    )

if __name__ == "__main__":
    iface.launch()
