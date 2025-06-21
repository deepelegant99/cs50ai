from openai import OpenAI
from dotenv import load_dotenv
import gradio as gr
import os

load_dotenv()

# This is a simple OpenAI client setup.

api_key = os.getenv("OPENAI_API_KEY")
# This code initializes an OpenAI client and prompts the user for input.
client = OpenAI(api_key=api_key)

system_prompt = "You are a helpful assistant."

# This code defines a function that sends a prompt to the OpenAI API and returns the response.
def respond (prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

gr.Interface(
    fn=respond,
    inputs=gr.Textbox(label="Enter your prompt"),
    outputs=gr.Textbox(label="Response from OpenAI"),
    title="OpenAI Chatbot",
    description="A simple chatbot using OpenAI's GPT-4o model."
).launch(share=True)

# print(response.choices[0].message.content)
# The response from the OpenAI API is printed to the console.

