import pytest
from screenplay import Actor
from abilities import browse_the_web
from actions_selenium import navigate_to, find_element
from os import path
from selenium.webdriver.common.by import By


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_an_element_that_exists_is_found_is_stored_and_returned():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'hello_id')).and_store_as('hello')
    )

    assert returned_value.text == 'hello'

    stored_value = user.state['hello'].value

    assert stored_value.text == 'hello'


@pytest.mark.slow
def test_finding_an_element_that_does_not_exists_stores_and_returns_None():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    returned_value = user.attempts_to(
        navigate_to(test_page),
        find_element((By.ID, 'does_not_exist')).and_store_as('hello')
    )

    assert returned_value is None

    stored_value = user.state['hello'].value

    assert stored_value is None
