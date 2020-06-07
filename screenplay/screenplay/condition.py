from .question import Question
from .matcher import Matcher


class Condition:
    def __init__(self, question: Question, expected: Matcher):
        self.question = question
        self.expected = expected
        self._successActions = []
        self._failureActions = []
        self._alwaysActions = []

    def if_they_do(self, *actions):
        self._successActions.extend(actions)
        return self

    def if_they_do_not(self, *actions):
        self._failureActions.extend(actions)
        return self

    def regardless_of_that(self, *actions):
        self._alwaysActions.extend(actions)
        return self

    def _run_actions_as(self, actor, actions):
        try:
            actor.attempts_to(*actions)
        except:
            pass

    def check_as(self, actor):
        try:
            assert self.expected.matches(self.question.answered_by(actor)), self.expected.fail_message
            self._run_actions_as(actor, self._successActions)
        except Exception as exception:
            self._run_actions_as(actor, self._failureActions)
            raise exception
        finally:
            self._run_actions_as(actor, self._alwaysActions)


see_that = Condition
