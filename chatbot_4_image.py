import PIL.Image
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
)

sample_file = PIL.Image.open('interior_design.jpg')

prompt = "How would you describe the style of this interior design?"

response = model.generate_content([prompt, sample_file])

print(response.text)