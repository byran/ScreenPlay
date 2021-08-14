from .task_or_action import TaskOrAction
from .log import log_message


class Action(TaskOrAction):
    @log_message('Action.performas not overridden')
    def perform_as(self, actor):
        pass
