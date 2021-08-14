from typing import Dict


class _ActorStateObject:
    def __init__(self):
        self._value = None
        self._value_set = False

    def set(self, value):
        self._value_set = True
        self._value = value

    @property
    def value(self):
        assert self._value_set, "Actor state accessed before it was set"
        return self._value


class ActorState:
    def __init__(self):
        self._state: Dict[str, _ActorStateObject] = {}

    def __getitem__(self, key):
        if key not in self._state:
            self._state[key] = _ActorStateObject()
        return self._state[key]


def value_of(x):
    if isinstance(x, _ActorStateObject):
        return x.value
    return x
