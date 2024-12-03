import requests
import json
from queue import Queue


class Node:
    name = ""
    traits = []
    description = ""

    def __init__(self, n, t, d):
        self.name = n
        self.traits = t
        self.description = d


class Graph:
    adjList = {}  # Adjacency list to contain edges
    nameMap = {}  # Maps game names to a node object

    def __init__(self):
        for pageNumber in range(0, 1):
            print(pageNumber)
            # response = requests.get("https://steamspy.com/api.php?request=all&page=" + str(pageNumber))
            response = requests.get("https://steamspy.com/api.php?request=top100forever")
            for game in response.json().values():  # Iterates through data
                traitList = []
                description = ""
                for trait in game.items():
                    if trait[0] != "name":
                        traitList.append(trait[1])  # Makes a list containing all relevant data for edge creation
                    if trait[0] == "appid":
                        link1 = "https://steamspy.com/api.php?request=appdetails&appid=" + str(trait[1])
                        response2 = requests.get(link1)
                        traitList.append(response2.json()["tags"])
                        link2 = "https://store.steampowered.com/api/appdetails?appids=" + str(trait[1])
                        response3 = requests.get(link2)
                        if response3.json() is None or not response3.json()[str(trait[1])]["success"]:
                            continue
                        description = response3.json()[str(trait[1])]["data"]["about_the_game"]

                self.nameMap[game["name"]] = Node(game["name"], traitList, description)
                self.adjList[game["name"]] = []
        self.initializeMatrix()
        print("DONE")

    def initializeMatrix(
            self):  # [NOT FINISHED] This function will be used to initialize the edges in the adjacency matrix
        for node in self.nameMap.values():
            for other in self.nameMap.values():
                if node.name != other.name and self.compareNodes(node, other) >= 11.0 and node.name not in self.adjList[
                    other.name]:
                    self.adjList[node.name].append(other.name)
                    self.adjList[other.name].append(node.name)

    def compareNodes(self, nodeOne, nodeTwo):  # [NOT FINISHED] This function will compare nodes to see if they are similar enough for an edge
        similarityScore = 0
        for index in range(2, 4):
            if nodeOne.traits[index] == nodeTwo.traits[index]:
                similarityScore += 0.75
        priceDiff = abs(int(nodeOne.traits[14]) - int(nodeTwo.traits[14])) / 10000.0
        similarityScore += 1 - priceDiff
        for tag in nodeOne.traits[1].items():
            if tag[0] in nodeTwo.traits[1]:
                similarityScore += 1
        # voteTotalOne = 0
        # for tag in nodeOne.traits[1].values():
        #     voteTotalOne += tag[0]
        # voteTotalTwo = 0
        # for tag in nodeTwo.traits[1].values():
        #     voteTotalTwo += tag[0]
        # for tag in nodeOne.traits[1].values():
        #     if nodeTwo.traits[1][tag[0]] == tag[1]:

        return similarityScore

    def printAdjacent(self, name):
        for game in self.adjList[name]:
            print(game)

    def getAdjacent(self, name):
        adj = [game for game in self.adjList[name]]
        adjGameObj = [self.nameMap[game] for game in adj]
        return adjGameObj

    def serialize_graph(self):
        return json.dumps(self.adjList)

    def bfs(self):
        source = next(iter(self.adjList))
        visited = {source}
        q = Queue()
        q.put(source)
        print("BFS: ")
        while not q.empty():
            u = q.get()
            print(u)
            neighbors = self.adjList[u]
            for v in neighbors:
                if v not in visited:
                    visited.add(v)
                    q.put(v)

    def recommend(self, likedGames):
        recs = {}
        result = []
        for game in likedGames:
            adj = self.getAdjacent(game)
            result += adj
        for game in result:
            present = False
            for item in recs.keys():
                if game.name == item:
                    present = True
                    recs[game.name]["frequency"] += 1
            if not present:
                info = {"description": game.description,
                        "frequency": 1,
                        "tags": game.traits}
                recs[game.name] = info
        return recs
    
    def storeGames(self):
        games = []
        for game in self.nameMap.items():
            name = game[0]
            description = game[1].description
            games.append((name, description))
            
        return games


