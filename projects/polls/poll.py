class Poll:
    def __init__(self, title: str, owner: str, _id: int = None):
        self.title = title
        self.owner = owner
        self._id = _id

    def __repr__(self) -> str:
        return f"Poll {self.title!r}, {self.owner!r}, {self._id!r}"