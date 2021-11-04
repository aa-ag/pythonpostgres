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
        connection.execute(CREATE_WATCHLIST_TABLE)


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


def watch_movie(username, title):
    with connection:
        connection.execute(DELETE_MOVIE, (title,))
        connection.execute(INSERT_WATCHED_MOVIE, (username, title))


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
CREATE_WATCHLIST_TABLE = """
CREATE TABLE IF NOT EXISTS watched (
    watcher_name TEXT,
    title TEXT,
    release_timestamp REAL
);
"""

# query to insert one movie into `movies` table
INSERT_MOVIES = """
INSERT INTO movies (title, release_timestamp) VALUES (?, ?);
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
SELECT * FROM watched WHERE watcher_name = ?;
"""

#  query to set watched movie
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 1 WHERE title = ?;"

# query to insert a watched movie
INSERT_WATCHED_MOVIE = "INSERT INTO watched (watcher_name, title) VALUES (?, ?);"

# query to delete a movie
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"