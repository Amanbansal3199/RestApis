from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:bansal31@localhost/RestApis'
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50), nullable=False)
    Release_date = db.Column(db.Date, nullable=False)

    def __init__(self, name, genre, Release_date):
        self.name = name
        self.genre = genre
        self.Release_date = Release_date

@app.route('/movies', methods=['POST'])
def Create_movie():
    Data = request.json
    name = Data.get("name")
    genre = Data.get("genre")
    Release_date = Data.get("Release_date")

    if name is not None and genre is not None and Release_date is not None:
        try:
            with app.app_context():
                movie = Movie(name=name, genre=genre, Release_date=Release_date)
                db.session.add(movie)
                db.session.commit()

                return {"message": "movie created successfully", "id": movie.id},201
        except IntegrityError:
            db.session.rollback()
            return {"message": "movie creation is failed (possibly duplicate)"}
            400
    else:
        return {"message":"invalid data"}, 400

@app.route("/movies", methods=["GET"])
def get_movies():
    data = Movie.query.all()
    movie_list = []
    # if data:
    for mov in data:
        movie_data = {
            "id": mov.id,
            "name": mov.name,
            "genre": mov.genre,
            "release_date": mov.Release_date.strftime("%Y-%m-%d")
        }
        movie_list.append(movie_data)
    return {"movie_list": movie_list},200
    # else:
    #     return {"message":"invalid response"}


@app.route("/movies/<int:id>", methods=["PUT"])
def movie_update(id):
    data = request.json

    name = data.get("name")

    genre = data.get("genre")

    Release_date = data.get("Release_date")

    if name is not None and genre is not None and Release_date is not None:
        movie = Movie.query.get(id)
        if movie:
            try:
                movie.name = name
                movie.genre =genre
                movie.Release_date = Release_date
                db.session.commit()

                return {"message": "Movie Updated Successfully","id": movie.id}, 200
            except IntegrityError:
                db.session.rollback()
                return {"message": "Movie Update failed"},400
        else:
            return {"message": "Movie not found"},404
    else:
        return {"message": "invalid data"}, 400

@app.route("/movies/<int:id>", methods=["DELETE"])
def Delete_Record(id):

    try:
        with app.app_context():
            movie = Movie.query.get(id)
            print(movie.name)
            if movie:
                db.session.delete(movie)
                db.session.commit()
                return {"message": "Movie deleted succesfully"},200
            else:
                return {"message": "Movie not found"},404
    except IntegrityError:
        db.session.rollback()
        return {"message": "movie deletion failed"},500


if __name__ == "__main__":
    app.run(debug=True)