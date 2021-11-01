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
    '''
     gets movie title from user, as well as a date in an expected format,
     then parses input into a date value, and writes that data into the db;
     raises an error of invalid format when that's the case
    '''
    title = input("Movie title:  ")
    release_date = input("Release date (dd-mm-YYYY):  ")
    try:
        parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
        timestamp = parsed_date.timestamp()
        db.add_movie(title, timestamp)
    except:
        print("Invalid date format, please try again.")


def print_movie_list(movies):
    '''
     grabs all movie titles and their dates from the db,
     transforms the date value into human readable format, and 
     prints out results into the console
    '''
    print("-- upcoming movies --\n")
    for movie in movies:
        movie_date = datetime.datetime.fromtimestamp(movie[1])
        human_readable_date = movie_date.strftime("%b %d, %Y")
        print(f"\"{movie[0]}\" (on {human_readable_date})")
    print("------------\n\n")


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
    movie_title = input("Enter a movie title you've already watched: ")
    db.watch_movie(username, movie_title)


############------------ DRIVER CODE ------------############
if __name__ == "__main__":    
    welcome_message = "Welcome to the movies' watchlist app:"
    print(welcome_message)

    db.create_tables()

    # until the user enters the number 6, the app
    # will run and keep expecting inputs 
    while (user_input := input(menu)) != "6":
        if user_input == "1":
            prompt_add_movie()

        elif user_input == "2":
            movies = db.get_movies(True)
            print_movie_list(movies)

        elif user_input == "3":
            movies = db.get_movies()
            print_movie_list(movies)

        elif user_input == "4":
            movies = db.get_movies()
            prompt_watch_movie()

        elif user_input == "5":
            username = input("username: ")
            movies = db.get_watched_movies(username)
            print_watched_movie_list(username, movies)
            
        else:
            print("************ Invalid input, please try again. ************")

    exit_message = "Thanks for using our app today: see you soon!"
    print(exit_message)