from typing import List
import database
import option
from connections import pool

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
        option.Option(option_text, self.id).save()

    def options(self) -> List[Option]:
        connection = create_connection()
        options = database.get_poll_opions(connection, self.id)
        connection.close()
        return [option.Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id) -> "Poll":
        connection = create_connection()
        poll = database.get_poll(connection, poll_id)
        connection.close()
        return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls) -> List["Poll"]:
        connection = create_connection()
        polls = database.get_polls(connection)
        connection.close()
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    @classmethod
    def latest(cls) -> "Poll":
        connection = create_connection()
        poll = database.get_latest_poll()
        connection.close()
        return cls(poll[1], poll[2], poll[0])