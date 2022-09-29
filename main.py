import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = input("> Input an idea: ")

while prompt != "":
    response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.85, max_tokens=500)
    print(response["choices"][0]["text"])

    prompt = input("> Input an idea: ")
