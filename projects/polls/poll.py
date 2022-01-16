from sqlite3 import connect
from typing import List
from models import Option
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

    def add_option(self, option_text: str):
        Option(option_text, self.id).save()

    def options(self) -> List[Option]:
        connection = create_connection()
        options = database.get_poll_opions(connection, self.id)
        connection.close()
        return [Option(option[1], option[2], option[0]) for option in options]