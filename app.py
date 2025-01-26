import os
import time
import warnings
from typing import Any

import requests
import streamlit as st
from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from utils.custom import css_code

# Suppress deprecated TensorFlow warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)

# Disable oneDNN optimizations if causing issues
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

load_dotenv(find_dotenv())
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

def progress_bar(amount_of_time: int) -> Any:
    """
    A simple progress bar that increases over time,
    then disappears when it reaches completion
    :param amount_of_time: time taken
    :return: None
    """
    progress_text = "Please wait, Generative models hard at work"
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(amount_of_time):
        time.sleep(0.04)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()

def generate_text_from_image(url: str) -> str:
    """
    A function that uses the BLIP model to generate text from an image.
    :param url: image location
    :return: text: generated text from the image
    """
    try:
        image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base", framework="pt")
        generated_text = image_to_text(url)[0]["generated_text"]
        
        # Ensure the generated text is a complete sentence.
        if not generated_text.endswith(('.', '!', '?')):
            generated_text += '.'  # Ensures ending as a complete thought.

        print(f"IMAGE INPUT: {url}")
        print(f"GENERATED TEXT OUTPUT: {generated_text}")
        return generated_text
    except Exception as e:
        print(f"Error in generating text from image: {e}")
        return "Failed to generate a complete description."

def expand_description(scenario: str) -> str:
    """
    A function that refines the description of the image by expanding on the details
    rather than generating a full story.
    :param scenario: the initial text generated from the image
    :return: a more detailed description of the image
    """
    try:
        # Use a pipeline for text generation, focusing on expanding the description
        model = pipeline("text-generation", model="gpt2", framework="pt")
        refined_description = model(f" {scenario}", max_length=200, num_return_sequences=1)[0]['generated_text']
        
        # Clean the generated description by ensuring it ends properly
        if not refined_description.endswith(('.', '!', '?')):
            refined_description += '.'

        print(f"TEXT INPUT: {scenario}")
        print(f"REFINED DESCRIPTION OUTPUT: {refined_description}")
        return refined_description
    except Exception as e:
        print(f"Error in refining description: {e}")
        return "Failed to refine description."

def generate_speech_from_text(message: str) -> Any:
    """
    A function using the ESPnet text-to-speech model from HuggingFace
    :param message: description of the image to convert into speech
    :return: generated audio from the description
    """
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
    payloads = {"inputs": message}

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open("generated_audio.flac", "wb") as file:
        file.write(response.content)

def main() -> None:
    """
    Main function that handles Streamlit UI and logic
    :return: None
    """
    st.set_page_config(page_title="IMAGE TO STORY CONVERTER", page_icon="🖼️")
    st.markdown(css_code, unsafe_allow_html=True)

    with st.sidebar:
        st.image("img/gkj.jpg")
        st.write("---")

    st.header("Image-Voice-AI")
    uploaded_file = st.file_uploader("Please choose a file to upload", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)
        progress_bar(100)

        # Generating the text from the image
        scenario = generate_text_from_image(uploaded_file.name)

        # Refining the image description into a more detailed account
        refined_description = expand_description(scenario)

        # Generating the speech from the refined description
        generate_speech_from_text(refined_description)

        with st.expander("Generated Image scenario"):
            st.write(scenario)
        with st.expander("Refined Description"):
            st.write(refined_description)

        # Playing the generated audio
        st.audio("generated_audio.flac")

if __name__ == "__main__":
    main()
