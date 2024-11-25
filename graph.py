import requests
import json

class Node:
    name = ""
    traits = []

    def __init__(self, n, t):
        self.name = n
        self.traits = t

class Graph:
    adjList = {} # Adjacency list to contain edges
    nameMap = {} # Maps game names to a node object
    def __init__(self):
        self.first = None
        response = requests.get("https://steamspy.com/api.php?request=top100forever")
        for game in response.json().values(): # Iterates through data
            traitList = []
            for trait in game.items():
                if trait[0] != "name":
                    traitList.append(trait[1]) # Makes a list containing all relevant data for edge creation
                if trait[0] == "appid":
                    link = "https://steamspy.com/api.php?request=appdetails&appid=" + str(trait[1])
                    response2 = requests.get(link)
                    traitList.append(response2.json()["tags"])

            self.nameMap[game["name"]] = Node(game["name"], traitList)
            print(game["name"])
            print(traitList)

    def initializeMatrix(self): # [NOT FINISHED] This function will be used to initialize the edges in the adjacency matrix
        for node in self.nameMap.values():
            for other in self.nameMap.values():
                None

    def compareNodes(self, nodeOne, nodeTwo): # [NOT FINISHED] This function will compare nodes to see if they are similar enough for an edge
        similarityScore = 0
        for index in range(2, 4):
            if nodeOne.traits[index] == nodeTwo.traits[index]:
                similarityScore += 1
        priceDiff = abs(int(nodeOne.traits[14]) - int(nodeTwo.traits[14]))/10000.0
        similarityScore += 1 - priceDiff
        for tag in nodeOne.traits[1].items():
            if tag[0] in nodeTwo.traits[1]:
                similarityScore += 1
                print(tag[0])
        # voteTotalOne = 0
        # for tag in nodeOne.traits[1].values():
        #     voteTotalOne += tag[0]
        # voteTotalTwo = 0
        # for tag in nodeTwo.traits[1].values():
        #     voteTotalTwo += tag[0]
        # for tag in nodeOne.traits[1].values():
        #     if nodeTwo.traits[1][tag[0]] == tag[1]:

        return similarityScore





