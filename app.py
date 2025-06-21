from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# This is a simple OpenAI client setup.

api_key = os.getenv("OPENAI_API_KEY")
# This code initializes an OpenAI client and prompts the user for input.
client = OpenAI(api_key=api_key)

user_prompt = input("Enter your prompt: ")

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a teaching assistant, and a dog."},
        {"role": "user", "content": user_prompt}
    ],
)

print(response.choices[0].message.content)
# The response from the OpenAI API is printed to the console.

