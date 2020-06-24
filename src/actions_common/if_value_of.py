from screenplay import Action, Actor


class if_value_of(Action):
    def __init__(self, id: str):
        super().__init__()
        self._id = id
        self._values = []
        self._actions = []

    def then(self, *actions):
        self._actions.extend(actions)
        return self

    def is_None(self):
        self._values.append(None)
        return self

    def equals(self, *values):
        self._values.extend(values)
        return self

    def perform_as(self, actor: Actor):
        if self._id is not None:
            value = actor.state[self._id].value
            for required_value in self._values:
                if value == required_value:
                    actor.attempts_to(*self._actions)
