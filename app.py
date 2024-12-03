from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():  # put application's code here
    return render_template('home.html')

@app.route('/recommender')
def recommender():  # put application's code here
    return render_template('recommender.html')

@app.route('/results')
def results():  # put application's code here
    return render_template('results.html')

@app.route('/topgames')
def topgames():  # put application's code here
    return render_template('topgames.html')


if __name__ == '__main__':
    app.run(debug=True)
