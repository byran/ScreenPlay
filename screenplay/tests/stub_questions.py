from screenplay import Question


class StubQuestion(Question):
    def __init__(self, answer):
        self.answer = answer

    def answered_by(self, actor):
        return self.answer
