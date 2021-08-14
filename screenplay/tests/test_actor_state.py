import pytest
from screenplay.actor_state import ActorState, value_of


def test_Accessing_a_previously_unset_state_key_returns_a_new_state_object():
    state = ActorState()

    o = state['Hello']

    assert o is not None


def test_The_value_set_in_a_state_object_can_be_retieived():
    state = ActorState()

    state['Hello'].set(486)

    assert state['Hello'].value == 486


def test_Multiple_values_can_br_set_and_retieived():
    state = ActorState()

    state['World'].set('!')
    state['Hello'].set(486)
    assert state['Hello'].value == 486
    assert state['World'].value == '!'


def test_Accessing_a_state_object_that_has_not_been_set_throws_an_assertion_error():
    state = ActorState()

    with pytest.raises(AssertionError):
        state['Bob'].value


def test_Getting_the_value_of_an_ActorStateObject_or_other_object_returns_the_correct_value():
    state = ActorState()

    state['Hello'].set(1234)

    a = state['Hello']
    b = 1234

    assert value_of(a) == 1234
    assert value_of(b) == 1234
