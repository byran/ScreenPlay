from screenplay import Task


class StubTask(Task):
    def __init__(self):
        self.called = False

    def perform_as(self, actor):
        self.called = True


class StubTaskWithResult(Task):
    def __init__(self, result):
        self.result = result

    def perform_as(self, actor):
        return self.result
