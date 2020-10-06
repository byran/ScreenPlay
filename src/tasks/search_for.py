from screenplay import Task, Actor, log_message
from actions_selenium import find_element, enter_text, send_enter_key_to
from pages.duckduckgo_homepage import duckduckgo_homepage


class search_for(Task):
    def __init__(self, text: str):
        super().__init__()
        self._text = text

    @log_message('Enter "{self._text}" into duckduckgo')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            find_element(duckduckgo_homepage.search_textbox).and_store_as('search_textbox')
            .if_nothing_is_found_fail_with_message('Unable to find search textbox'),
            enter_text(self._text).into_stored_element('search_textbox'),
            send_enter_key_to().stored_element('search_textbox')
        )
