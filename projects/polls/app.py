############------------ IMPORTS ------------############
import psycopg2
from psycopg2.errors import DivisionByZero
import database
import settings


############------------ GLOBAL VARIABLE(S) ------------############
MENU_PROMPT = """
-- MENU --
(1) create a poll
(2) list open polls
(3) vote on a poll
(4) show poll votes
(5) select a random winner from a poll option
(6) exit

Enter your choice:
"""

NEW_OPTION_PROMPT = "Enter new option text (or leave empty to stop adding options):"


MENU_OPTIONS = {
    "1": prompt_create_poll,
    "2": list_open_polls,
    "3": prompt_vote_poll,
    "4": show_poll_votes,
    "5": randomize_poll_winner
}

############------------ FUNCTION(S) ------------############
def prompt_create_poll(connection):
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll owner: ")
    options = list()

    while new_option := input(NEW_OPTION_PROMPT):
        options.append(new_option)

    database.create_poll(connection, poll_title, poll_owner, options)


def list_open_polls(connection):
    polls = database.get_polls(connection)

    for id_, title, owner in polls:
        print(f"{id_}: {title}, created by {owner}")


def prompt_vote_poll(connection):
    poll_id = int(input("Enter poll would you like to vote on: "))
    poll_options = database.get_poll_details(connection, poll_id)
    print_poll_options(poll_options)

    option_id = int(input("Enter the option you'd like to vote for: "))
    username = input("Enter voter's username: ")
    database.add_poll_vote(connection, username, option_id)


def print_poll_options(poll_options):
    for option in poll_options:
        print(f"{option[3]}: {option[4]}")


def show_poll_votes(connection):
    poll_id = int(input("Enter poll you'd like to see votes for."))
    try:
        poll_and_votes = database.get_poll_and_results(connection, poll_id)
    except DivisionByZero:
        print("Poll has received no votes yet")
    else:
        for _id, option_text, count, percentage in poll_and_votes:
            print(f"{option_text} got {count} votes ({percentage:.2f}% of total)")


def randomize_poll_winner(connection):
    poll_id = int(input("Enter poll id of poll you'd like to pick a winner for: "))
    poll_options = database.get_poll_details(connection, poll_id)
    print_poll_options(poll_options)

    option_id = int(input("Enter which is the winning option, we'll pick a random winner from votes: "))
    winner = database.get_random_poll_vote(connection, option_id)
    print(f"The randomly selected winner is {winner[0]}.")


def app_run():
    database_uri = settings.postgres_url
    connection = psycopg2.connect(database_uri)

    while (selection := input(MENU_PROMPT)) != "6":
        try:
            MENU_OPTIONS[selection](connection)
        except KeyError:
            print("Invalid input selected. Try again.")

    
############------------ DRIVER CODE ------------############
