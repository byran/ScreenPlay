"""Example file containing a minimum implementation of a Task"""

from screenplay import Task, Actor, log_message


class template_task(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # A parameter list of Action objects
        )
