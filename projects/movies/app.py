############------------ IMPORTS ------------############
import datetime
import database as db


############------------ GLOBAL ------------############
menu = """
Please select one of the following options:
(1) Add new movie.
(2) View upcoming movies.
(3) View all movies.
(4) Watch a movie.
(5) View watched movies.
(6) Add new user.
(7) Exit.\n\n
"""


############------------ FUNCTIONS ------------############
def prompt_add_movie():
    '''
     gets movie title from user, as well as a date in an expected format,
     then parses input into a date value, and writes that data into the db;
     raises an error of invalid format when that's the case
    '''
    title = input("Movie title:  ")
    release_date = input("Release date (mm-dd-YYYY):  ")
    parsed_date = datetime.datetime.strptime(release_date, "%m-%d-%Y")
    timestamp = parsed_date.timestamp()
    db.add_movie(title, timestamp)


def print_movie_list(heading, movies):
    '''
     grabs all movie titles and their dates from the db,
     transforms the date value into human readable format, and 
     prints out results into the console
    '''
    print(f"-- {heading} movies --")

    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%d %b %Y")
        print(f"{_id}: {title} (on {human_date})")

    print("---- \n")


def print_watched_movie_list(username, movies):
    print(f"-- {username}'s watched the following movies: ")
    for movie in movies:
        print(f"{movie[1]}")
    print("--- \n")


def prompt_watch_movie():
    '''
     udpates "watched" flag in db for movies already watched
    '''
    username = input("Username:  ")
    movie_id = input("Movie ID: ")
    db.watch_movie(username, movie_id)


def prompt_add_user():
    username = input("Username: ")
    db.add_user(username)


def prompt_show_watched_movies():
    username = input("username: ")
    movies = db.get_watched_movies(username)
    if movies:
        print_movie_list("Watched", movies)
    else:
        print(f"User \"{username}\" hasn't watched any movies.")


############------------ DRIVER CODE ------------############
if __name__ == "__main__":    
    welcome_message = "Welcome to the movies' watchlist app:"
    print(welcome_message)

    db.create_tables()

    # until the user enters the number 7, the app
    # will run and keep expecting inputs 
    while (user_input := input(menu)) != "7":
        if user_input == "1":
            prompt_add_movie()

        elif user_input == "2":
            movies = db.get_movies(True)
            print_movie_list("Upcoming", movies)

        elif user_input == "3":
            movies = db.get_movies()
            print_movie_list("All", movies)

        elif user_input == "4":
            movies = db.get_movies()
            prompt_watch_movie()

        elif user_input == "5":
            prompt_show_watched_movies()

        elif user_input == "6":
            prompt_add_user()
            
        else:
            print("************ Invalid input, please try again. ************")

    exit_message = "Thanks for using our app today: see you soon!"
    print(exit_message)