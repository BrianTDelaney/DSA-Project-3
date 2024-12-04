from graph import Graph
from ai import generate_prompt
from heap import Heap

# games = Graph() # THIS CODE WILL TAKE A MINUTE TO RUN
# input = ["Portal 2", "Half-Life 2", "Counter-Strike: Global Offensive"]
# print(games.recommend(input))
# games.printAdjacent("Half-Life")

user_input = input("What type of games do you like?\n")
output = generate_prompt(user_input)
print(output)

# games = Heap()
# games.bfs()a l
