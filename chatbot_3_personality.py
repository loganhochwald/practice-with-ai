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
    safety_settings=safety_settings,
    system_instruction="You are another student who is learning Python but you are optimistic about the learning process. You should give me reassurance when I don't understand something. Don't offer to help."
)

# Generate a response
response = model.generate_content("Man, this project has been really difficult!")
print(response.text)
