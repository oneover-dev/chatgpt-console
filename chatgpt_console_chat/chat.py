import os
import openai
from dotenv import load_dotenv 

load_dotenv(dotenv_path=os.path.join('API_key', 'API_KEY.env'))

openai.api_key = os.getenv("OPENAI_API_KEY")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": user_input}]
    )
    print("ChatGPT:", response['choices'][0]['message']['content'])
