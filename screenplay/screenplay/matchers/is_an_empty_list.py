from ..matcher import Matcher
from typing import List


class _IsAnEmptyListMatcher(Matcher):
    def matches(self, answer: List) -> bool:
        length = len(answer)
        if length == 0:
            return True
        self._fail_message = "List is not empty, it contains {length} elements".format(length=length)
        return False


def is_an_empty_list():
    return _IsAnEmptyListMatcher()
