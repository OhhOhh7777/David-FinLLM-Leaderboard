import gradio as gr
from textblob import TextBlob

def text_analysis(text):
    # Sentiment analysis
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else (
        "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    )
    
    # Word count
    word_count = len(text.split())
    
    # Character count
    char_count = len(text)
    
    return sentiment, word_count, char_count

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Text Analysis Tool")
    gr.Markdown("Enter your text below to analyze its sentiment, word count, and character count.")
    
    with gr.Row():
        input_text = gr.Textbox(label="Enter your text here", lines=5, placeholder="Type something...")
    
    with gr.Row():
        sentiment_output = gr.Textbox(label="Sentiment")
        word_count_output = gr.Textbox(label="Word Count")
        char_count_output = gr.Textbox(label="Character Count")
    
    analyze_button = gr.Button("Analyze Text")
    
    # Connect the function to Gradio interface
    analyze_button.click(
        text_analysis, 
        inputs=input_text, 
        outputs=[sentiment_output, word_count_output, char_count_output]
    )

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
