from screenplay import Actor
from abilities import browse_the_web
from actions_selenium import navigate_to, find_elements, find_stored_element_in
from os import path
from selenium.webdriver.common.by import By


test_page = 'file://' + path.join(path.dirname(__file__), 'elements.html')


def test_a_sub_element_can_be_found_by_its_text():
    user = Actor.named('user').who_can(browse_the_web.using_Chrome())

    user.attempts_to(
        navigate_to(test_page),
        find_elements((By.CSS_SELECTOR, '#list li')).and_store_as('list_elements')
    )

    returned_value = user.attempts_to(
        find_stored_element_in('list_elements').with_text_equal_to('third_li').and_store_as('found')
    )

    assert returned_value.text == 'third_li'

    stored_value = user.state['found'].value

    assert stored_value.text == 'third_li'
