from screenplay.matchers.contains import contains


def test_The_contains_matcher_returns_True_if_the_answer_contains_the_expected_value():
    assert contains(1).matches([1, 2, 3, 4]), "The matcher failed to match even though the value was in the list"
    assert contains(3).matches([1, 2, 3, 4]), "The matcher failed to match even though the value was in the list"


def test_The_contains_matcher_returns_False_if_the_answer_does_not_contain_the_expected_value():
    assert contains(2).matches([1, 4, 6]) is False, "The matcher matched even though the value is not in the list"


def test_The_contains_matcher_failure_message_indicates_the_failure():
    matcher = contains(1)
    matcher.matches([])

    assert matcher._fail_message == 'none of the items were "1"'
