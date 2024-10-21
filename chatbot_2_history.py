import google.generativeai as genai
from model_settings import safety_settings
from model_settings import model_name
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Create the generative model with safety settings
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings
)

# Function to get user input and store the conversation
def chat_with_ai():
    conversation_log = []  # List to store the conversation

    while True:
        # Get user input
        user_input = input("You: ")

        # Exit the loop if the user types "exit"
        if user_input.lower() == "exit":
            break

        # Generate AI response
        response = model.generate_content(user_input)

        # Store user input and AI response in the conversation log
        conversation_log.append({"user": user_input, "ai": response.text})

        # Display the AI response
        print(f"AI: {response.text}")


# Start the chat
chat_with_ai()
