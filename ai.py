from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# from OpenAI documentation
def generate_prompt(task_or_prompt: str):
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "Give the user video game recommendations based on their description of the games they like, and make sure to choose the highest rated games.",
            },
            {
                "role": "user",
                "content": "Task, Goal, or Current Prompt:\n" + task_or_prompt,
            },
        ],
    )
    return completion.choices[0].message.content


user_input = input("What type of games do you like?\n")

generate_prompt(user_input)