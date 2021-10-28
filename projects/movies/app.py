############------------ IMPORTS ------------############
import datetime
from sqlite3.dbapi2 import Timestamp
import database as db


############------------ GLOBAL ------------############
menu = """
Please select one of the following options:
(1) Add new movie.
(2) View upcoming movies.
(3) View all movies.
(4) Match a movie.
(5) View watched movies.
(6) Exit.
"""


############------------ FUNCTIONS ------------############
def add_movie():
    title = input("Movie title:  ")
    release_date = input("Release date (dd/mm/yyyy):  ")
    parsed_date = datetime.datetime.strptime(release_date, "%d/%m/%Y")
    timestamp = parsed_date.timestamp()
    db.add_movie(title, timestamp)


############------------ DRIVER CODE ------------############
welcome_message = "Welcome to the movies' watchlist app:"
print(welcome_message)

db.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        pass
    if user_input == "2":
        pass
    if user_input == "3":
        pass
    if user_input == "4":
        pass
    if user_input == "5":
        pass
    else:
        print("Invalid input, please try again.")