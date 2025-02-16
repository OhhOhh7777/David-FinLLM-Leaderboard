#!/usr/bin/env python
"""
Grayscale Image Converter
This program demonstrates the use of Gradio's Blocks API along with Pillow to convert an image to grayscale.
"""

import gradio as gr
from PIL import Image, ImageOps

def convert_to_grayscale(image):
    """
    Convert the provided image to grayscale.
    
    Args:
        image (PIL.Image): The input image.
        
    Returns:
        PIL.Image: The grayscale version of the image.
    """
    if image is None:
        return None
    # Convert the image to grayscale using Pillow's ImageOps
    grayscale_image = ImageOps.grayscale(image)
    return grayscale_image

# Build the Gradio interface using Blocks
with gr.Blocks(title="Grayscale Image Converter") as demo:
    gr.Markdown("# Grayscale Image Converter")
    gr.Markdown("Upload an image to convert it to grayscale.")
    
    # Layout: two columns for input and output components
    with gr.Row():
        with gr.Column():
            image_input = gr.Image(label="Input Image", type="pil")
            convert_button = gr.Button("Convert")
        with gr.Column():
            image_output = gr.Image(label="Grayscale Image")
    
    # Set up the event: when the button is clicked, run the conversion function
    convert_button.click(
        fn=convert_to_grayscale,
        inputs=image_input,
        outputs=image_output
    )
    
    gr.Markdown("**Note:** This app uses the Pillow library for image processing.")

# Launch the Gradio app
if __name__ == "__main__":
    demo.launch()
