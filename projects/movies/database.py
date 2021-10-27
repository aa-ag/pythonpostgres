############### QUERIES
# query to create `movies` table
CREATE_MOVIES_TABLE = """
CREATE TABLE IF NOT EXISTS movies (
    title TEXT,
    release_timestamp REAL,
    watched INTEGER
);
"""

# query to insert one movie into `movies` table
INSERT_MOVIES = """
INSERT INTO movies (title, released_timestamp, watched) VALUES (?, ?, 0);
"""
