from flask import Flask, render_template, request, jsonify
from graph import Graph
from heap import Heap
import json
from collections import OrderedDict

app = Flask(__name__)
gameGraph = None

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    print("BING")
    return render_template('home.html')

@app.route('/recommender')
def recommender():  # put application's code here
    global gameGraph
    if gameGraph is None:
        gameGraph = Graph()
    return render_template('recommender.html')

@app.route('/results', methods=["POST", "GET"])
def results():  # put application's code here
    print(request.method)
    if request.method == "POST":
        data = request.get_json()
        print(data)
        data = data['data']
        global gameGraph
        result = gameGraph.recommend(data)
        print(result)
        return render_template('results.html', data=result)
    else:
        return render_template('results.html')

@app.route('/topgames')
def topgames():  # put application's code here
    return render_template('topgames.html')

if __name__ == '__main__':
    app.run(debug=True)
