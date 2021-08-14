from ..matcher import Matcher
from typing import List


class _DoesNotContainMatcher(Matcher):
    def __init__(self, expected, fail_message_format='one of the items was "{expected}"'):
        super().__init__()
        self.expected = expected
        self.fail_message_format = fail_message_format

    def matches(self, answer: List) -> bool:
        if answer.count(self.expected) == 0:
            return True
        self._fail_message = self.fail_message_format.format(expected=self.expected)
        return False


def does_not_contain(expected):
    return _DoesNotContainMatcher(expected)
