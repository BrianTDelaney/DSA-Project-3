from graph import Graph
from ai import generate_prompt

games = Graph() # THIS CODE WILL TAKE A MINUTE TO RUN, ALSO STILL ONLY LOOKS AT TOP 1000 GAMES
# games.printAdjacent("Half-Life")

serialized_graph = games.serialize_graph()

user_input = input("What type of games do you like?\n")
print(generate_prompt(user_input))
