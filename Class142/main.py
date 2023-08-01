from flask import Flask, request, jsonify
import csv

allMovies = []

with open("movies2.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    allMovies = data[1:]

liked_movies = []
unliked_movies = []
movies_notwatched = [] 

app = Flask(__name__)
@app.route("/get-movie")

def get_movie():
    return jsonify({
        "data": allMovies[0],
        "status": "Success"
    })

@app.route("/liked-movie", methods = ["POST"])
def liked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    liked_movies.append(movie)

    return jsonify({
        "status": "Success"
    }), 201

@app.route("/unliked-movie", methods = ["POST"])
def unliked_movie():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    unliked_movies.append(movie)

    return jsonify({
        "status": "Success"
    }), 201

@app.route("/movie-notwatched", method = ["POST"])
def movie_notwatched():
    movie = allMovies[0]
    allMovies = allMovies[1:]
    movies_notwatched.append(movie)

    return jsonify({
        "status": "Success"
    }), 201

if __name__ == "__main__":
    app.run()