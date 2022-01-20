############------------ IMPORT(S) ------------############
from sqlite3 import connect
from typing import List, Tuple
from psycopg2 import execute_values


############------------ GLOBAL ------------############
Poll = Tuple[int, str, str]
Vote = Tuple[str, int]
Option = Tuple[int, str, int]


############------------ FUNCTION(S) ------------############
def create_tables(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_POLLS)
        cursor.execute(CREATE_OPTIONS)
        cursor.execute(CREATE_VOTES)


def get_polls(connection) -> List[Poll]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_POLLS)
        return cursor.fetchall()


def get_poll(connection, poll_id: int) -> Poll:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_POLL, (poll_id))
        return cursor.fetchone()

def get_latest_poll(connection) -> List[PollWithOption]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_LATEST_POLL)
        return cursor.fetchall()


def get_poll_options(connection, poll_id: int) -> List[Option]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_POLLS_OPTIONS, (poll_id,))
        return cursor.fetchall()


def create_poll(connection, title: str, owner: str, options: List[str]):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_POLL_RETURN_ID, (title, owner))

        poll_id = cursor.fetchone()[0]
        option_values = [(option_text, poll_id) for option_text in options]
        
        execute_values(cursor, INSERT_OPTION, option_values)


def add_poll_vote(connection, username: str, option_id: int):
    with connection:
        cursor = connection.cursor()
        cursor.execute(INSERT_VOTE, (username, option_id))


def get_option(connection, option_id: int) -> Option:
    pass


def add_option(connection, option_text, poll_id: int):
    pass


def get_votes_for_options(connection, option_id: int) -> List[Vote]:
    pass


############------------ QUERIES(S) ------------############
CREATE_POLLS = """
CREATE TABLE IF NOT EXISTS polls 
(id SERIAL PRIMARY_KEY, title TEXT, owner_username TEXT)';
"""

CREATE_OPTIONS = """
CREATE TABLE IF NOT EXISTS options
(id SERIAL PRIMARY_KEY, option_text TEXT, poll_id INTEGER, 
FOREIGN_KEY(poll_id) REFERENCES polls (id));
"""

CREATE_VOTES = """
CREATE TABLE IF NOT EXISTS votes
(username TEXT, option_id INTEGER, FOREIGN KEY(option_id) REFERENCES options (id));
"""

SELECT_ALL_POLLS = """
SELECT * FROM polls;
"""

SELECT_POLLS_OPTIONS = """
SELECT * FROM options
WHERE poll_id = %s;
"""

SELECT_LATEST_POLL = """
SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = (
    SELECT id FROM polls ORDER BY id DESC LIMIT 1
);
"""

INSERT_OPTION = """
INSERT INTO options (option_text, poll_id) VALUES %s;
"""

INSERT_VOTE = """
INSERT INTO votes (username, option_id) VALUES (%s, %s);
"""

INSERT_POLL_RETURN_ID = "INSERT INTO polls (title, owner_username) VALUES (%s, %s) RETURNING id;"

SELECT_VOTE_FOR_OPTIONS = "SELECT * FROM votes WHERE option_id = %s"

SELECT_POLL = "SELECT * FROM polls WHERE id = %s;"