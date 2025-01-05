import gradio as gr
from transformers import pipeline

# Load pre-trained sentiment-analysis model (DistilBERT)
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
classifier = pipeline("sentiment-analysis", model=model_name)

# Define the prediction function without the slider
def sentiment_analysis(text):
    # Perform sentiment analysis
    result = classifier(text)
    sentiment = result[0]['label']
    score = result[0]['score']
    
    # Return sentiment and confidence score
    return f"Sentiment: {sentiment} (Confidence: {score:.2f})"


# Create Gradio Interface
interface = gr.Interface(
    fn=sentiment_analysis,
    inputs=[
        gr.Textbox(lines=2, placeholder="Enter text here...", label="Input Text", interactive=True),
    ],
    outputs="text",
    title="Sentiment Analysis Tool",
    description="This tool predicts whether the sentiment of the given text is Positive, Negative, or Neutral. It also provides a confidence score for the prediction.",
    examples=[
        ["I love spending time with my family!"],
        ["This weather is terrible."],
        ["The movie was okay, not great but not bad."]
    ],
    theme="compact",  # Use Gradio's compact theme
    css=".gradio-container { background-color: #f4f4f9; padding: 20px; border-radius: 10px; }"  # Custom CSS for styling
)

# Launch the app
if __name__ == "__main__":
    interface.launch()
