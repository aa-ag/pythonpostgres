############------------ IMPORTS ------------############
import datetime
import database as db


############------------ GLOBAL ------------############
menu = """
Please select one of the following options:
(1) Add new movie.
(2) View upcoming movies.
(3) View all movies.
(4) Match a movie.
(5) View watched movies.
(6) Exit.\n\n
"""


############------------ FUNCTIONS ------------############
def prompt_add_movie():
    title = input("Movie title:  ")
    release_date = input("Release date (dd-mm-YYYY):  ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()
    db.add_movie(title, timestamp)


def print_movie_list(movies):
    print("-- upcoming movies --")
    for movie in movies:
        print(f"{movie[0]} (on {movie[1]})")
    print("------------\n\n")


############------------ DRIVER CODE ------------############
welcome_message = "Welcome to the movies' watchlist app:"
print(welcome_message)

db.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again.")