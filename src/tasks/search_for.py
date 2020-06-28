from screenplay import Task, Actor, log_message
from actions_selenium import enter_text, send_enter_key_to
from pages.google_homepage import google_homepage


class search_for(Task):
    def __init__(self, text: str):
        super().__init__()
        self._text = text

    @log_message('Enter \'{self._text}\' into google')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into_element(google_homepage.search_textbox),
            send_enter_key_to().element(google_homepage.search_textbox)
        )
