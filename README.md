## Image-Voice-AI
Image-Voice-AI is a Streamlit web application that leverages Hugging Face models for generating text from images, refining that text, and converting it into speech. This app allows users to upload an image, generate a descriptive story, enhance that story, and then listen to the generated description through text-to-speech.

## Features
Image to Text: Convert images into descriptive text using the BLIP model.
Text Refinement: Expand and refine the generated text description using the GPT-2 model.
Speech Generation: Convert the refined text into speech using Hugging Face's ESPnet model.
Progress Bar: A visual progress indicator as the models work on the input.
Audio Playback: Play the generated speech for the user.

## Requirements
To run the project, you need to have the following Python dependencies installed:

Python 3.8 or higher
requests
streamlit==1.20.0
python-dotenv
transformers==4.24.0
torch==1.13.1
huggingface_hub
You can install the dependencies using the following command:

bash
Copy
pip install -r requirements.txt
Setup Instructions
Clone the Repository: Clone the repository to your local machine:

bash
Copy
git clone https://github.com/Avanishsingh7/Image-Voice-AI.git
cd Image-Voice-AI

## Install Dependencies: Install the required Python libraries:

bash
Copy
pip install -r requirements.txt

## Environment Setup: Create a .env file in the root directory of your project and add your Hugging Face API Token:

bash
Copy
HUGGINGFACE_API_TOKEN=your_huggingface_api_token
Run the Application: You can now run the Streamlit app:

bash
Copy
streamlit run app.py
This will open the app in your default web browser.

## How it Works
Upload an Image: Once the app is running, you can upload an image using the file uploader in the Streamlit sidebar.

Image-to-Text: The app uses the BLIP model from Hugging Face to generate a description of the uploaded image.

Text Refinement: After the image is processed, the app uses GPT-2 to refine the generated text, expanding upon the details.

Text-to-Speech: The refined description is then passed to a Hugging Face model (ESPnet) for text-to-speech conversion, and the resulting audio is provided for playback.

Progress Indicator: A progress bar is shown while the models work on the input, ensuring the user knows the app is processing the image and generating the content.

## File Structure
graphql
Copy
Image-Voice-AI/
├── app.py                # Main application logic and UI (Streamlit)
├── custom.py             # Custom CSS for Streamlit UI styling
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (e.g., Hugging Face API token)
├── img/                  # Image assets for the app (e.g., logo)

## Customization
CSS Customization: The app uses custom CSS (defined in custom.py) to adjust padding and margins for better layout management.
Hugging Face Models: The app leverages the Hugging Face pipeline for various NLP and image processing models. You can change or update these models based on your needs.

## Contribution
Feel free to fork the repository and submit issues or pull requests. Contributions are welcome!

## Fork the repository.
Create a new branch.
Make your changes.
Open a pull request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
