from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/ranker')
def ranker():  # put application's code here
    return render_template('ranker.html')

@app.route('/recommender')
def recommender():  # put application's code here
    return render_template('recommender.html')


if __name__ == '__main__':
    app.run(debug=True)
