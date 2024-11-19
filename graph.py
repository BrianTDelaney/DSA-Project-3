import requests
import json

class Node:
    name = ""
    traits = []

    def __init__(self, n, t):
        name = n
        traits = t

class Graph:
    adjMatrix = [[]] # Adjacency matrix to contain edges
    nameMap = {} # Maps game names to an index and a node object
    def __init__(self):
        self.first = None
        response = requests.get("https://steamspy.com/api.php?request=top100forever")
        for game in response.json().values(): # Iterates through data
            traitList = []
            for trait in game.items():
                if trait[0] != "name" and trait[0] != "appid":
                    traitList.append(trait[1]) # Makes a list containing all relevant data for edge creation

            newNode = Node(game["name"], traitList)
            self.nameMap[game["name"]] = (len(self.nameMap), newNode)

    def initializeMatrix(self): # [NOT FINISHED] This function will be used to initialize the edges in the adjacency matrix
        for node in self.nameMap.values():
            for other in self.nameMap.values():
                None

    def compareNodes(self, nodeOne, nodeTwo): # [NOT FINISHED] This function will compare nodes to see if they are similar enough for an edge
        similarityScore = 0
