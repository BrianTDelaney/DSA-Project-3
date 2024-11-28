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
                "content": "The following is a graph represented as an adjacency list: {serialized_graph} Give the user video game recommendations based on their description of the games they like, and make sure to choose the highest rated games. Do not choose the same games the user mentions. The graph is arranged so that the most similar games have are adjacent to each other.",
            },
            {
                "role": "user",
                "content": "Description of games I like:\n" + task_or_prompt,
            },
        ],
        max_tokens=150
    )
    return completion.choices[0].message.content
