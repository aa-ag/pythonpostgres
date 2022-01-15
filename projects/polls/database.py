############------------ IMPORT(S) ------------############
from typing import List, Tuple
from psycopg2 import execute_values


############------------ GLOBAL ------------############
Poll = Tuple[int, str, str]
Vote = Tuple[str, int]
PollWithOption = Tuple[int, str, str, int, str, int]
PollResults = Tuple[int, str, int, float]


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


def get_latest_poll(connection) -> List[PollWithOption]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_LATEST_POLL)
        return cursor.fetchall()


def get_poll_details(connection, poll_id: int) -> List[PollWithOption]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_POLLS_WITH_OPTIONS, (poll_id,))
        return cursor.fetchall()


def get_poll_and_vote_results(connection, poll_id: int) -> List[PollResults]:
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_POLL_VOTE_DETAILS, (poll_id,))


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

SELECT_POLLS_WITH_OPTIONS = """
SELECT * FROM polls
JOIN options ON polls.id = options.poll_id
WHERE polls.id = %s;
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

SELECT_POLL_VOTE_DETAILS = """
SELECT 
    options.id,
    options.option_text,
    COUNT(votes.option_id) AS vote_count,
    COUNT(votes.option_id) / SUM(COUNT(votes.option_id)) OVER() * 100.0 AS vote_percentage
FROM options
LEFT JOIN votes ON options_id = votes.option_id
WHERE options.poll_id = %s
GROUP BY options.id;
"""