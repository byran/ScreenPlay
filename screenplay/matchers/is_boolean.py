from ..matcher import Matcher


class _Booleanatcher(Matcher):
    def __init__(self, expected: bool):
        super().__init__()
        self.expected = expected
        self.fail_message_format = 'Answer is not {expected}'

    def matches(self, answer) -> bool:
        if answer == self.expected:
            return True
        self._fail_message = self.fail_message_format.format(expected=self.expected)
        return False


def is_true():
    return _Booleanatcher(True)


def is_false():
    return _Booleanatcher(False)
