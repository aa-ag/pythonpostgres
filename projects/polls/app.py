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

############------------ DRIVER CODE ------------############
