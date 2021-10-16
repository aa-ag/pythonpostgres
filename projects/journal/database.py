# import sqlite3
import sqlite3

# create a connection to the sqlite connection
connection = sqlite3.connect("data.db")


def create_table():
    # uses the sqlite3 connection to create a table
    # executing SQL command
    connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")
    connection.commit()



def add_entry(entry_content, entry_date):
    # append info as dictionary into entries list
    connection.execute(
        f"INSERT INTO entries VALUES (?, ?);", \
            (entry_content, entry_date)
        )


def get_entries():
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM entries;")
    ### alternatively:
    cursor = connection.execute("SELECT * FROM entries;")
    # return a list of all results from query
    cursor.fetchall()
