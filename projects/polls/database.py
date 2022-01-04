############------------ IMPORTS ------------############


############------------ GLOBAL VARIABLE(S) ------------############


############------------ QUERIES(S) ------------############
CREATE_POLLS = """
CREATE TABLE IF NOT EXISTS polls 
(id SERIAL PRIMARY_KEY, title TEXT, owner_username TEXT)';
"""
