import pytest
from screenplay import Actor
from actions_common import select_element_at_index


def test_selecting_an_element_from_a_stored_list_returns_the_value_and_stores_it_in_the_actors_state():
    user = Actor('user')
    user.state['list'].set(['a', 'b', 'c', 'd'])

    returned_value = user.attempts_to(
        select_element_at_index(1).from_stored_list('list').and_store_in('found')
    )

    assert returned_value == 'b', "Returned value was incorrect"
    assert user.state['found'].value == 'b', "Stored value was incorrect"


def test_an_attempted_out_of_bounds_access_causes_an_assertion():
    user = Actor('user')
    user.state['list'].set(['a'])

    with pytest.raises(AssertionError) as exception:
        user.attempts_to(
            select_element_at_index(1).from_stored_list('list').and_store_in('found')
        )

    expected = "'list' does not have enough elements to access element 1"
    actual = exception.value.args[0]

    assert actual == expected, "Incorrect message\nExpected: {expected}\nActual:{actual}".format(
        expected=expected, actual=actual)
