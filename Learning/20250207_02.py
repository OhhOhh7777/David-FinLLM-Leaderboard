import gradio as gr

# Define the basic math functions
def basic_operations(number1, number2):
    addition = number1 + number2
    subtraction = number1 - number2
    multiplication = number1 * number2
    division = number1 / number2 if number2 != 0 else "Division by zero error"
    return addition, subtraction, multiplication, division

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# Basic Math Operations")
    gr.Markdown("Enter two numbers below to perform addition, subtraction, multiplication, and division.")
    
    with gr.Row():
        number1 = gr.Number(label="Number 1")
        number2 = gr.Number(label="Number 2")
    
    with gr.Row():
        addition_output = gr.Textbox(label="Addition Result")
        subtraction_output = gr.Textbox(label="Subtraction Result")
        multiplication_output = gr.Textbox(label="Multiplication Result")
        division_output = gr.Textbox(label="Division Result")
    
    calculate_button = gr.Button("Calculate")
    
    # Link the function with the interface
    calculate_button.click(
        basic_operations,
        inputs=[number1, number2],
        outputs=[addition_output, subtraction_output, multiplication_output, division_output]
    )

# Launch the app
if __name__ == "__main__":
    demo.launch()
