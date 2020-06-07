from screenplay import Action, Actor
from typing import Any


class fail_with_message(Action):
    def __init__(self, message: str):
        super().__init__()
        self._message = message
        self._id = None
        self._failValues = []

    def if_value_of(self, id: str):
        self._id = id
        return self

    def is_None(self):
        self._failValues.append(None)
        return self

    def equals(self, failValue: Any):
        self._failValues.append(failValue)
        return self

    def perform_as(self, actor: Actor):
        assert False, self._message
