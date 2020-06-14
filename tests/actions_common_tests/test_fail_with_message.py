import pytest
from screenplay import Actor
from actions_common import fail_with_message


def test_fail_with_message_causes_an_assertion():
    user = Actor.named('user')

    with pytest.raises(AssertionError) as exception:
        user.attempts_to(
            fail_with_message('simple message')
        )
    
    assert exception.value.args[0] == 'simple message'
