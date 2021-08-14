from .task_or_action import TaskOrAction
from .log import log_message


class Task(TaskOrAction):
    @log_message('Task.performas not overridden')
    def perform_as(self, actor):
        pass
