from screenplay import Action, Actor


class _equals_if_value_of(Action):
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


class _not_equals_if_value_of(Action):
    def __init__(self, id: str):
        super().__init__()
        self._id = id
        self._values = []
        self._actions = []

    def then(self, *actions):
        self._actions.extend(actions)
        return self

    def is_not_None(self):
        self._values.append(None)
        return self

    def does_not_equal_any_of(self, *values):
        self._values.extend(values)
        return self

    def perform_as(self, actor: Actor):
        if self._id is not None:
            value = actor.state[self._id].value
            matched = False
            for required_value in self._values:
                if value == required_value:
                    matched = True
            if matched is False:
                actor.attempts_to(*self._actions)


class if_value_of():
    def __init__(self, id: str):
        super().__init__()
        self._id = id

    def is_None(self):
        return _equals_if_value_of(self._id).is_None()

    def equals(self, *values):
        return _equals_if_value_of(self._id).equals(*values)

    def is_not_None(self):
        return _not_equals_if_value_of(self._id).is_not_None()

    def does_not_equal_any_of(self, *values):
        return _not_equals_if_value_of(self._id).does_not_equal_any_of(*values)

    def perform_as(self, actor: Actor):
        assert False, "No values specified in if_value_of task"
