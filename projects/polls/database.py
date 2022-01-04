############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############


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