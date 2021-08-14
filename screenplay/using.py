from screenplay import Task, Actor
from screenplay.task_or_action import TaskOrAction


class Using(Task):
    def __init__(self, task_or_action: TaskOrAction):
        self.task_or_action = task_or_action
        self.id = None

    def perform_as(self, actor: Actor):
        assert self.id is not None, "No id specified for Using"
        actor.state[self.id].set(actor.attempts_to(
            self.task_or_action
        ))

    def as_(self, id):
        self.id = id
        return self


using = Using
