import google.generativeai as genai
from model_settings import safety_settings
from model_settings import model_name
import os
from dotenv import load_dotenv
import speech_recognition as sr

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Create the generative model with safety settings
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings,
)

# Set up the recognizer
recognizer = sr.Recognizer()

def recognize_speech_and_generate_response():
    while True:
        try:
            with sr.Microphone() as source:
                print("I'm listening. (Say 'stop' to end the chat)")
                audio = recognizer.listen(source)

                # Convert speech to text
                spoken_text = recognizer.recognize_google(audio)
                print(f"Your prompt: {spoken_text}")

                # Check for exit command
                if spoken_text.lower() == "stop":
                    print("Ending the chat. Goodbye!")
                    break

                # Generate a response using the generative model
                response = model.generate_content(spoken_text)
                print(f"AI: {response.text}")

        except sr.UnknownValueError:
            print("Could not understand the audio. Please try again.")
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")

recognize_speech_and_generate_response()
