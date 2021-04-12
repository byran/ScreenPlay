from screenplay import Actor, Action
from screenplay.actions import if_value_of


class record_if_run(Action):
    def __init__(self):
        self.triggered = False

    def perform_as(self, actor: Actor):
        self.triggered = True


def test_if_a_value_is_None_then_the_actions_are_run():
    user = Actor.named('user')
    action = record_if_run()

    user.state['not_set'].set(None)

    user.attempts_to(
        if_value_of('not_set').is_None().then(
            action
        )
    )

    assert action.triggered, "Action was not triggered"


def test_if_a_value_is_set_then_the_actions_are_not_run():
    user = Actor.named('user')
    action = record_if_run()

    user.state['not_set'].set(1)

    user.attempts_to(
        if_value_of('not_set').is_None().then(
            action
        )
    )

    assert not action.triggered, "Action was triggered"


def test_if_a_value_is_1_and_the_required_is_1_then_the_actions_are_run():
    user = Actor.named('user')
    action = record_if_run()

    user.state['not_set'].set(1)

    user.attempts_to(
        if_value_of('not_set').equals(1).then(
            action
        )
    )

    assert action.triggered, "Action was not triggered"


def test_if_a_value_is_2_and_the_required_is_1_or_2_then_the_actions_are_run():
    user = Actor.named('user')
    action = record_if_run()

    user.state['not_set'].set(2)

    user.attempts_to(
        if_value_of('not_set').equals(2).then(
            action
        )
    )

    assert action.triggered, "Action was not triggered"
