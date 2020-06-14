from screenplay import Actor
from abilities import browse_the_web
from actions_selenium import navigate_to, find_element, text_of
from os import path
from selenium.webdriver.common.by import By


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_the_text_of_a_stored_element_is_stored_and_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello'),
        text_of().stored_element('hello').and_store_as('text')
    )

    assert returned_value == 'hello'

    stored_value = user.state['text'].value

    assert stored_value == 'hello'


def test_the_text_of_a_stored_element_is_only_returned_if_no_request_to_store_is_requested():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello'),
        text_of().stored_element('hello')
    )

    assert returned_value == 'hello'


def test_stripping_the_text_removes_whitespace():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'world_id')).and_store_as('world'),
        text_of().stored_element('world').stripped_of_whitespace().and_store_as('text')
    )

    assert returned_value == 'world'

    stored_value = user.state['text'].value

    assert stored_value == 'world'
