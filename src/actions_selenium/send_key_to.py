"""Functions to create Action objects to send keys to webpage elements"""

from screenplay import Action, Actor, log_message
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from abilities.browse_the_web import browser_for


class _send_key_to_element(Action):
    def __init__(self, locator, key: Keys, key_name: str):
        self._locator = locator
        self._key = key
        self._key_name = key_name

    @log_message('Send key \'{self._key_name}\' to element "{self._locator}"')
    def perform_as(self, actor: Actor):
        element: WebElement = browser_for(actor).find_element(*self._locator)
        element.send_keys(self._key)


class _send_key_to_stored_element(Action):
    def __init__(self, id, key: Keys, key_name: str):
        self._id = id
        self._key = key
        self._key_name = key_name

    @log_message('Send key \'{self._key_name}\' to element "{self._id}"')
    def perform_as(self, actor: Actor):
        actor.state[self._id].value.send_keys(self._key)


class send_enter_key_to:
    def element(self, locator):
        """
        Creates an Action object to send the enter key to the specified element

        Arguments:

        locator - A tuple with the first element is a selenium By value and the
        second a string to specify the id/tag/etc...
        """
        return _send_key_to_element(locator, Keys.ENTER, 'Enter')

    def stored_element(self, id: str):
        """
        Creates an Action object to send the enter key to the stored element

        Arguments:

        id - The Id of the stored element
        """
        return _send_key_to_stored_element(id, Keys.ENTER, 'Enter')
