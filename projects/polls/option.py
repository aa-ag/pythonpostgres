from typing import List
from connection import create_connection
import database


class Option:
    def __init__(self, option_text: str, poll_id: int, _id: int = None):
        self.id = _id,
        self.text = option_text
        self.poll_id = poll_id

    def __repr__(self) -> str:
        return f"Option {self.text!r}, {self.poll_id!r}, {self.id!r}"