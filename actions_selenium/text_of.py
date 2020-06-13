from screenplay import Action, Actor, log_message


class _text_of_stored_element(Action):
    def __init__(self, id: str):
        super().__init__()
        self._id = id
        self._stripWhitespace = False

    def stripped_of_whitespace(self):
        self._stripWhitespace = True
        return self

    @log_message('Get text of stored element \'{self._id}\'')
    def perform_as(self, actor: Actor):
        text = actor.state[self._id].value.text

        if self._stripWhitespace:
            text = text.strip()

        return text


class text_of:
    def stored_element(self, id: str):
        return _text_of_stored_element(id)
