############------------ IMPORTS ------------############
import option
import poll
import psycopg2
from psycopg2.errors import DivisionByZero
import database
from projects.polls.database import Option
import settings
from typing import List


############------------ FUNCTION(S) ------------############
def prompt_create_poll():
    poll_title = input("Enter poll title: ")
    poll_owner = input("Enter poll owner: ")
    new_poll = poll.Poll(poll_title, poll_owner)
    new_poll.save()

    while new_option := input(NEW_OPTION_PROMPT):
        new_poll.add_option(new_option)


def list_open_polls():
    open_polls = poll.Poll.all()

    for open_poll in open_polls:
        print(f"{open_poll.id}: {open_poll.title}, created by {open_poll.owner}")


def prompt_vote_poll():
    poll_id = int(input("Enter poll would you like to vote on: "))
    poll_options = poll.Poll.get(poll_id).options
    print_poll_options(poll_options)

    option_id = int(input("id:"))
    username = input("username:")
    Option.get(option_id).vote(username)


def print_poll_options(poll_options: List[Option]):
    for option in poll_options:
        print(f"{option.id}: {option.text}")


def show_poll_votes():
    poll_id = int(input("Enter poll you'd like to see votes for."))
    try:
        poll_and_votes = database.get_poll_and_results(connection, poll_id)
    except DivisionByZero:
        print("Poll has received no votes yet")
    else:
        for _id, option_text, count, percentage in poll_and_votes:
            print(f"{option_text} got {count} votes ({percentage:.2f}% of total)")


def randomize_poll_winner():
    poll_id = int(input("Enter poll id of poll you'd like to pick a winner for: "))
    poll_options = database.get_poll_details(connection, poll_id)
    print_poll_options(poll_options)

    option_id = int(input("Enter which is the winning option, we'll pick a random winner from votes: "))
    winner = database.get_random_poll_vote(connection, option_id)
    print(f"The randomly selected winner is {winner[0]}.")


def app_run():
    database_uri = settings.postgres_url
    connection = create_connection()

    while (selection := input(MENU_PROMPT)) != "6":
        try:
            MENU_OPTIONS[selection]()
        except KeyError:
            print("Invalid input selected. Try again.")


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

############------------ DRIVER CODE ------------############
if __name__ == "__main__":
    app_run()