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
    try:
        parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = parsed_date.timestamp()
        db.add_movie(title, timestamp)
    except:
        print("Invalid date format, please try again.")


def print_movie_list(movies):
    print("-- upcoming movies --\n")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_readable_date = movie_date.strftime("%b %d, %Y")
        print(f"\"{movie[0]}\" (on {human_readable_date})")
    print("------------\n\n")


def prompt_watch_movie():
    movie_title = input("Enter a movie title you've already watched")
    db.watch_movie(movie_title)


############------------ DRIVER CODE ------------############
welcome_message = "Welcome to the movies' watchlist app:"
print(welcome_message)

db.create_tables()

while (user_input := input(menu)) != "6":
    if user_input == "1":
        prompt_add_movie()
    elif user_input == "2":
        movies = db.get_movie(True)
        print_movie_list(movies)
    elif user_input == "3":
        pass
    elif user_input == "4":
        pass
    elif user_input == "5":
        pass
    else:
        print("Invalid input, please try again.")