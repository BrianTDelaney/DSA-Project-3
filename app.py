from flask import Flask, render_template, request, jsonify
from graph import Graph
from heap import Heap
import time
import json
from collections import OrderedDict

app = Flask(__name__)
gameGraph = None
gameHeap = None
recs = None

@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/recommender', methods=["POST", "GET"])
def recommender():  # put application's code here
    global gameGraph
    if request.method == "POST":
        data = request.get_json()
        print(data)
        data = data['data']
        result = gameGraph.recommend(data)
        global recs
        recs = json.dumps(result)
        print("YOUR RECS")
        print(recs)
        return render_template('recommender.html')
    else:
        start = time.time()
        if gameGraph is None:
            gameGraph = Graph()
        duration = time.time() - start
        duration = json.dumps({'time': round(duration, 2)})
        result = json.dumps(list(gameGraph.nameMap.keys()))
        print(result)
        return render_template('recommender.html', data=result, time=duration)

@app.route('/results')
def results():  # put application's code here
    global recs
    return render_template('results.html', data=recs)

@app.route('/topgames')
def topgames():  # put application's code here
    global gameHeap
    start = time.time()
    if gameHeap is None:
        gameHeap = Heap()
    duration = time.time() - start
    duration = json.dumps({'time': round(duration, 2)})
    result = gameHeap.heap
    result = json.dumps(result)
    print(result)
    return render_template('topgames.html', data=result, time=duration)

if __name__ == '__main__':
    app.run(debug=True)
