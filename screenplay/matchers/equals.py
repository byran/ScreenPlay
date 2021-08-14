from ..matcher import Matcher


class _EqualsMatcher(Matcher):
    def __init__(self, expected, fail_message_format='{actual} is not equal to {expected}'):
        super().__init__()
        self.expected = expected
        self.fail_message_format = fail_message_format

    def matches(self, answer) -> bool:
        if answer == self.expected:
            return True
        self._fail_message = self.fail_message_format.format(actual=answer, expected=self.expected)
        return False


def is_(expected):
    return _EqualsMatcher(expected, '{actual} is not {expected}')


def equals(expected):
    return _EqualsMatcher(expected)
