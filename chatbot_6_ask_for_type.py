import google.generativeai as genai
from model_settings import safety_settings
from model_settings import model_name
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Ask the user what kind of chatbot they want
chatbot_type = input("What kind of chatbot do you want? Send the prompt here: ")

# Create the generative model with safety settings and user-defined instruction
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings,
    system_instruction=f"This is your prompt: {chatbot_type}"
)

while True:
    # Get user input
    user_input = input("You: ")

    # Check if the user wants to stop
    if user_input.lower() == "stop":
        print("Chatbot: Goodbye!")
        break

    # Generate a response
    response = model.generate_content(user_input)
    print(f"Chatbot: {response.text}")
