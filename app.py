# Import necessary libraries
import requests  # For making HTTP requests
import io  # For handling byte data
from PIL import Image  # For image processing
import gradio as gr  # For creating the web interface

# Define the API URL for the Hugging Face model
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"

# Set the headers for the API request, including the authorization token
headers = {"Authorization": "Bearer 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"}

# Define a function to query the API with the user's prompt
def query(prompt):
    # Create a payload with the user's input
    payload = {"inputs": prompt}

    # Make a POST request to the API with the payload and headers
    response = requests.post(API_URL, headers=headers, json=payload)

    # Return the content of the response (the generated image in bytes)
    return response.content

# Define a function to handle the image generation and display the image
def generate_image(prompt):
    # Call the query function to get the image bytes based on the user's prompt
    image_bytes = query(prompt)

    # Open the image bytes as an image using PIL
    image = Image.open(io.BytesIO(image_bytes))

    # Resize the image to a smaller size
    image = image.resize((256, 256))

    # Return the generated image
    return image

# Create the Gradio Interface using the text-to-image template
with gr.Blocks() as demo:
    gr.Markdown("<h1 style='text-align: center; font-family: 'Arial', sans-serif'>o1-painter | CWJ</h1>")
    with gr.Row():
        with gr.Column(scale=1, min_width=500):
            prompt = gr.Textbox(label="Enter your prompt", placeholder="Type something here...")
            generate_button = gr.Button("Generate")
            output_image = gr.Image(type="pil", label="Generated Image")
            gr.Examples(
                examples=[
                    ["Astronaut in a jungle, cold color palette, muted colors, detailed, 8k"],
                    ["An cat riding a green horse"],
                    ["Dogs playing football"],
            ],
            inputs=prompt
            )
        

    generate_button.click(fn=generate_image, inputs=prompt, outputs=output_image)

# Launch the Gradio Interface
demo.launch(share=True)
