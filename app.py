from flask import Flask, render_template, request
from recommendations import random_recommender

app = Flask(__name__, static_url_path = '/static')

@app.route("/")
def homepage():
    return render_template("homepage.html", title = "Hello Awesome Movie Viewer!")

@app.route("/recs")
def recommendations():
    form = request.args
    results = random_recommender()
    return render_template("recommendations.html", movies = results, votes = form)

if __name__ == '__main__':
    app.run(debug = True)