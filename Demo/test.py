import gradio as gr

def greet(name):
    return f"Hello, {name}!"

with gr.Blocks() as demo:
    # This HTML block includes the Ionicons CDN links and uses an ion-icon element.
    gr.HTML("""
    <h1>Gradio with Ionicons</h1>
    <p>Here's a heart icon: <ion-icon name="heart-outline" style="font-size:48px;"></ion-icon></p>
    <!-- Include Ionicons CSS and JS -->
    <script type="module" src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.esm.js"></script>
    <script nomodule src="https://unpkg.com/ionicons@7.1.0/dist/ionicons/ionicons.js"></script>
    """)
    
    # A simple text input and output example
    name_input = gr.Textbox(label="Your Name")
    greet_button = gr.Button("Greet")
    greet_output = gr.Text(label="Greeting")
    
    greet_button.click(fn=greet, inputs=name_input, outputs=greet_output)

demo.launch()