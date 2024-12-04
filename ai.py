from openai import OpenAI
from dotenv import load_dotenv
from graph import Graph
import json
import os

load_dotenv()

games = Graph()
arrayGames = games.storeGames()
formatted_json = json.dumps(arrayGames, indent=2)

# from OpenAI documentation
def generate_prompt(task_or_prompt: str):
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    completion = client.chat.completions.create(
        model="chatgpt-4o-latest",
        messages=[
            {
                "role": "system",
                "content": f"Recommend games based strictly on this json formatted list that has games with their descriptions: {formatted_json} Give the user video game recommendations based on their description of the games they like, and make sure the game is not outside of the provided list. Do not choose the same games the user mentions. Also do not put descriptions. Recommend 5 games if possible, and less if there are not many games that match the preferences. Put a comma between each game. Example Output: Dark Souls 3, Elden Ring, Sekiro. Only select from the games listed above based on their descriptions. Do not invent or suggest games outside of the list under any circumstances.",
            },
            {
                "role": "user",
                "content": "Description of games I like:\n" + task_or_prompt,
            },
        ],
        max_tokens=200
    )
    return completion.choices[0].message.content
