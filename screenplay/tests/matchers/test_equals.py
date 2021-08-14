from screenplay.matchers.equals import equals


def test_The_equals_matcher_returns_True_if_the_answer_is_equal_to_the_expected():
    assert equals(1).matches(1), "Two equal values were not classed as equal"


def test_The_equals_matcher_returns_False_if_the_answer_is_not_equal_to_the_expected():
    assert equals(2).matches(1) is False, "Two different values were classed as equal"


def test_The_equals_matcher_failure_message_indicates_the_failure():
    matcher = equals(3)
    matcher.matches(4)

    assert matcher._fail_message == '4 is not equal to 3'
