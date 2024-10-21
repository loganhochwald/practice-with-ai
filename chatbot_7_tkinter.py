import google.generativeai as genai
import os
from dotenv import load_dotenv
import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk  # Using ttk for styling
from model_settings import safety_settings
from model_settings import model_name

# Load environment variables from the .env file
load_dotenv()

# Configure the generative AI model
genai.configure(api_key=os.environ["API_KEY"])

# Create the generative model with safety settings
model = genai.GenerativeModel(
    model_name=model_name,
    safety_settings=safety_settings,
    system_instruction="Send plain text only."
)

# Function to send the user's input to the generative model and get a response
def send_prompt():
    user_input = user_entry.get()
    if user_input:
        # Display user input in the conversation box
        conversation_box.insert(tk.END, f"You: {user_input}\n", 'user')

        # Send the input to the model
        response = model.generate_content(user_input)

        # Display AI response in the conversation box
        conversation_box.insert(tk.END, f"Chatbot: {response.text}\n", 'ai')
        conversation_box.see(tk.END)  # Scroll to the end of the conversation

        # Clear the input field after sending the prompt
        user_entry.delete(0, tk.END)

# Set up the main application window with a dark background
window = tk.Tk()
window.title("Chat with AI")
window.geometry("600x600")
window.configure(bg="#222831")

# Style the conversation box with tags for user and AI text
def style_conversation_box():
    conversation_box.tag_config('user', foreground='#FFD369', font=('Arial', 10, 'bold'))  # User messages in gold
    conversation_box.tag_config('ai', foreground='#EEEEEE', font=('Arial', 10))  # AI messages in light gray

# Create a styled conversation box
conversation_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=70, height=20, state='normal', bg="#393E46", fg="#FFFFFF", font=('Arial', 12))
conversation_box.pack(padx=10, pady=10)
style_conversation_box()

# Frame to hold input and send button
input_frame = tk.Frame(window, bg="#222831")
input_frame.pack(padx=10, pady=10, fill=tk.X)

# Create an input field for the user to type their prompts
user_entry = ttk.Entry(input_frame, width=60, font=('Arial', 12))
user_entry.pack(side=tk.LEFT, padx=10, pady=5, expand=True)

# Create another frame to center the "Talk to AI" button
button_frame = tk.Frame(window, bg="#222831")
button_frame.pack(padx=10, pady=5)

# Create a styled "Talk to AI" button and center it
send_button = ttk.Button(button_frame, text="Send", command=send_prompt, style='SendButton.TButton')
send_button.pack(padx=10, pady=5)

# Apply some button styling
style = ttk.Style()
style.configure('SendButton.TButton', font=('Helvetica', 12), background="#FFD369", foreground="#393E46")
style.map('SendButton.TButton', background=[('active', '#FFC947')])

# Run the Tkinter event loop
window.mainloop()
