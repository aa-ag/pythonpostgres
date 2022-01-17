from sqlite3 import connect
from typing import List
from venv import create
from connection import create_connection
import database


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id,
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option {self.text!r}, {self.poll_id!r}, {self.id!r}"

    def save(self):
        connection = create_connection()
        new_option_id = database.add_option(connect, option_id)
        connection.close()
        self.id = new_option_id

    
