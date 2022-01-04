############------------ GLOBAL VARIABLE(S) ------------############


############------------ FUNCTION(S) ------------############
def create_tables(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(CREATE_POLLS)
        cursor.execute(CREATE_OPTIONS)
        cursor.execute(CREATE_VOTES)


def get_polls(connection):
    with connection:
        cursor = connection.cursor()
        cursor.execute(SELECT_ALL_POLLS)
        return cursor.fetchall()


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

INSERT_OPTION = """
INSERT INTO options (option_text, poll_id) VALUES %s;
"""

INSERT_VOTE = """
INSERT INTO votes (username, option_id) VALUES (%s, %s);
"""