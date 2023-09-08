import streamlit as st
import openai
import requests
from PIL import Image
from io import BytesIO
import shutil
import base64

# Set your OpenAI API key
api_key = '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'

# Initialize the OpenAI API client
openai.api_key = api_key

st.title('Generate your own clothes as you want')

# Input prompt
prompt = st.text_input('Enter a prompt:')
image_size = st.selectbox("Image Size (pixels)", [1024, 512, 256])
if st.button('Generate Image'):
    # Create an image using the OpenAI DALL-E API
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=f"{image_size}x{image_size}"
    )

    # Extract the image URL from the API response
    image_url = response['data'][0]['url']

    # Download and display the generated image
    image_response = requests.get(image_url)
    if image_response.status_code == 200:
        image_data = Image.open(BytesIO(image_response.content))
        st.image(image_data, caption='Generated Image', use_column_width=True)

        # Provide a download button for the image
        download_button = st.download_button(
            label="Download Image",
            data=image_response.content,
            file_name="generated_image.png",
            key="download_button"
        )
