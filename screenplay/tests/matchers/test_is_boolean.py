from screenplay.matchers.is_boolean import is_true, is_false


def test_The_is_true_matcher_returns_True_if_the_answer_is_True():
    assert is_true().matches(True), "The matcher failed to match even though the value was True"


def test_The_is_true_matcher_returns_False_if_the_answer_is_False():
    assert is_true().matches(False) is False, "The matcher matched even though the value was False"


def test_The_is_true_matcher_failure_message_indicates_the_failure():
    matcher = is_true()
    matcher.matches(False)

    assert matcher._fail_message == 'Answer is not True'


def test_The_is_false_matcher_returns_True_if_the_answer_is_False():
    assert is_false().matches(False), "The matcher failed to match even though the value was False"


def test_The_is_false_matcher_returns_False_if_the_answer_is_True():
    assert is_false().matches(True) is False, "The matcher matched even though the value was True"


def test_The_is_false_matcher_failure_message_indicates_the_failure():
    matcher = is_false()
    matcher.matches(True)

    assert matcher._fail_message == 'Answer is not False'
