#!/usr/bin/env python
"""
Simple Chatbot Simulator
This program demonstrates Gradio's Chatbot component by echoing user messages and allowing chat history to be cleared.
"""

import gradio as gr

def generate_response(message, history):
    """
    Update the chat history with the user's message and a simple echo response.
    
    Args:
        message (str): The user's input message.
        history (list): The chat history (list of tuples).
        
    Returns:
        tuple: Updated chat history and an empty string to reset the input.
    """
    if history is None:
        history = []
    history.append(("User", message))
    history.append(("Bot", f"Echo: {message}"))
    return history, ""

def clear_chat():
    """
    Clear the chat history.
    
    Returns:
        list: An empty list to reset the chat.
    """
    return [], ""

# Build the Gradio interface using Blocks
with gr.Blocks(title="Simple Chatbot Simulator") as demo:
    gr.Markdown("# Simple Chatbot Simulator")
    gr.Markdown("Interact with the chatbot. It will echo your messages back to you.")
    
    # Chatbot component to display conversation history
    chatbot = gr.Chatbot(label="Chat History")
    
    # Row layout for the text input and buttons
    with gr.Row():
        user_input = gr.Textbox(placeholder="Type your message here...", label="Your Message")
        send_button = gr.Button("Send")
        clear_button = gr.Button("Clear Chat")
    
    # State to maintain the conversation history
    chat_state = gr.State([])
    
    # Event for sending a message
    send_button.click(
        fn=generate_response,
        inputs=[user_input, chat_state],
        outputs=[chatbot, user_input]
    )
    
    # Allow submission by pressing Enter
    user_input.submit(
        fn=generate_response,
        inputs=[user_input, chat_state],
        outputs=[chatbot, user_input]
    )
    
    # Event for clearing the chat
    clear_button.click(
        fn=clear_chat,
        inputs=None,
        outputs=[chatbot]
    )
    
    gr.Markdown("**Note:** This chatbot echoes your input and supports clearing the chat history.")

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
