from .question import Question
from .matcher import Matcher


class Condition:
    def __init__(self, question: Question, expected: Matcher):
        self.question = question
        self.expected = expected
        self._failureActions = []

    def if_they_do_not(self, *actions):
        self._failureActions.extend(actions)
        return self

    def _run_failure_actions_as(self, actor):
        try:
            actor.attempts_to(*self._failureActions)
        except:
            pass

    def check_as(self, actor):
        try:
            assert self.expected.matches(self.question.answered_by(actor)), self.expected.fail_message
        except Exception as exception:
            self._run_failure_actions_as(actor)
            raise exception


see_that = Condition
