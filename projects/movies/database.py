############------------ IMPORTS ------------############
import datetime
import sqlite3
from sqlite3.dbapi2 import Cursor


############------------ GLOBAL ------------############
connection = sqlite3.connect("data.db")


############------------ FUNCTIONS ------------############
def create_tables():
    with connection:
        connection.execute(CREATE_MOVIES_TABLE)
        connection.execute(CREATE_USERS_TABLE)
        connection.execute(CREATE_WATCHED_TABLE)


def add_user(useraname):
    with connection:
        connection.execute(INSERT_USER, (useraname,))


def add_movie(title, release_timestamp):
    with connection:
        connection.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        cursor = connection.cursor()
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def watch_movie(username, movie_id):
    with connection:
        connection.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()


############------------ QUERIES ------------############
# query to create `movies` table
CREATE_MOVIES_TABLE = """
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY
    title TEXT,
    release_timestamp REAL
);
"""

CREATE_USERS_TABLE = """
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY
);
"""

# query to create the watchlist table 
CREATE_WATCHED_TABLE = """
CREATE TABLE IF NOT EXISTS watched (
    user_username TEXT,
    movie_id INTEGER,
    FOREIGN KEY(user_username) REFERENCES movies(id)
    FOREIGN KEY(movie_id) REFERENCES movies(id)
);
"""

# query to insert one movie into `movies` table
INSERT_MOVIES = """
INSERT INTO movies (title, release_timestamp) VALUES (?, ?);
"""

# query to insert a new user
INSERT_USER = """
INSERT INTO users (username) VALUES (?)
"""

# query to read/display all movies saved into the `movies` table
SELECT_ALL_MOVIES = """
SELECT * FROM movies;
"""

# query to read/display movies that meet a timestamp condition
SELECT_UPCOMING_MOVIES = """
SELECT * FROM movies WHERE release_timestamp > ?;
"""

# query to read/display moves that have already been watched
SELECT_WATCHED_MOVIES = """
SELECT * 
FROM movies
JOIN watched ON movies.id = watched.movie_id
JOIN users ON users.username = watched.user_username
WHERE users.username = ?;
"""

#  query to set watched movie
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"

# query to insert a watched movie
INSERT_WATCHED_MOVIE = "INSERT INTO watched (user_username, movie_id) VALUES (?, ?);"

# query to delete a movie
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"