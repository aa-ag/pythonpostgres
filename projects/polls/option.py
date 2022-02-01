from datetime import datetime
from typing import List
from connection_pool import get_connection
import database
import pytz


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id,
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option {self.text!r}, {self.poll_id!r}, {self.id!r}"

    def save(self):
        connection = get_connection()
        new_option_id = database.add_option(connection, self.option_id)
        self.id = new_option_id

    @classmethod
    def get(cls, option_id: int) -> "Option":
        connection = get_connection()
        option = database.get_option(connection, option_id)
        return cls(option[1], option[2], option[0])

    def vote(self, username: str):
        connection = get_connection()
        current_datetime_utc = datetime.datetime.now(tz=pytz.utc)
        current_timestamp = current_datetime_utc.timestamp()
        database.add_poll_vote(connection, self.id, current_timestamp)

    @property
    def votes(self) -> List[database.Vote]:
        connection = get_connection()
        votes = database.get_votes_for_options(connection, self.id)
        return votes
