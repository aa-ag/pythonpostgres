from socket import create_connection
from sqlite3 import connect
import database


class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.title = title
        self.owner = owner
        self._id = _id

    def __repr__(self) -> str:
        return f"Poll {self.title!r}, {self.owner!r}, {self._id!r}"

    def save(self):
        connection = create_connection()
        new_poll_id = database.create_poll(connection, self.title, self.owner)
        connection.close()
        self.id = new_poll_id