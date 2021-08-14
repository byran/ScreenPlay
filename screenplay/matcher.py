class Matcher:
    def __init__(self):
        self._fail_message = 'Matcher fail message not specified'

    def matches(self, answer) -> bool:
        return False

    @property
    def fail_message(self):
        return self._fail_message
