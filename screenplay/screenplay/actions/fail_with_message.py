from screenplay import Action, Actor


class fail_with_message(Action):
    def __init__(self, message: str):
        super().__init__()
        self._message = message

    def perform_as(self, actor: Actor):
        assert False, self._message
