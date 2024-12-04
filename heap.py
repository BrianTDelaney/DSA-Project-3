import requests
import json
import math
from queue import Queue

class Heap:
    heap = []
    ratings = {}

    def __init__(self):
        for pageNumber in range(0, 1):
            # print(pageNumber)
            # response = requests.get("https://steamspy.com/api.php?request=all&page=" + str(pageNumber))
            response = requests.get("https://steamspy.com/api.php?request=top100forever")
            for game in response.json().values():
                link1 = "https://steamspy.com/api.php?request=appdetails&appid=" + str(game["appid"])
                response2 = requests.get(link1)
                name = game["name"]
                pos = int(game["positive"])
                neg = int(game["negative"])
                if "Utilities" in response2.json()["tags"].keys():
                    continue
                total = pos + neg
                self.heap.append(name)
                self.ratings[name] = (pos, pos/total)
                self.heapifyUp()

    def heapifyUp(self):
        index = len(self.heap) - 1
        while index > 0:
            parentIndex = math.floor((index - 1)/2)
            parent = self.heap[parentIndex]
            current = self.heap[index]
            ratioDiff = abs(self.ratings[parent][1] - self.ratings[current][1])
            # print(parent)
            # print(self.ratings[parent])
            # print(current)
            # print(self.ratings[current])
            if (self.ratings[parent][1] < self.ratings[current][1] and ratioDiff > 0.075) or (ratioDiff < 0.075 and self.ratings[parent][1] < self.ratings[current][1] and self.ratings[parent][0] < self.ratings[current][0]):
                # print("SWAP")
                temp = self.heap[parentIndex]
                self.heap[parentIndex] = current
                self.heap[index] = temp
            else:
                # print("NO SWAP")
                break
            index = parentIndex

    def getTop(self):
        return self.heap[0]

    def bfs(self):
        for item in self.heap:
            print(item)