from cmath import polar
from typing import List
import database
import option
from connection_pool import get_connection
from option import Option

class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.title = title
        self.owner = owner
        self._id = _id

    def __repr__(self) -> str:
        return f"Poll {self.title!r}, {self.owner!r}, {self._id!r}"

    def save(self):
        connection = get_connection()
        new_poll_id = database.create_poll(connection, self.title, self.owner)
        self.id = new_poll_id

    def add_option(self, option_text: str):
        option.Option(option_text, self.id).save()

    def options(self) -> List[Option]:
        connection = get_connection()
        options = database.get_poll_opions(connection, self.id)
        return [option.Option(option[1], option[2], option[0]) for option in options]

    @classmethod
    def get(cls, poll_id) -> "Poll":
        connection = get_connection()
        poll = database.get_poll(connection, poll_id)
        return cls(poll[1], poll[2], poll[0])

    @classmethod
    def all(cls) -> List["Poll"]:
        connection = get_connection()
        polls = database.get_polls(connection)
        return [cls(poll[1], poll[2], poll[0]) for poll in polls]

    @classmethod
    def latest(cls) -> "Poll":
        connection = get_connection()
        poll = database.get_latest_poll()
        return cls(poll[1], poll[2], poll[0])