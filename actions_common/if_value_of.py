from screenplay import Action, Actor
from typing import Any


class if_value_of(Action):
    def __init__(self, id: str):
        super().__init__()
        self._id = id
        self._failValues = []
        self._actions = []

    def then(self, *actions):
        self._actions.extend(actions)
        return self

    def is_None(self):
        self._failValues.append(None)
        return self

    def equals(self, failValue: Any):
        self._failValues.append(failValue)
        return self

    def perform_as(self, actor: Actor):
        if self._id is not None:
            value = actor.state[self._id].value
            for failValue in self._failValues:
                if value == failValue:
                    actor.attempts_to(*self._actions)
