from typing import List
from .ability import Ability
from .condition import Condition
from .task_or_action import TaskOrAction
from .action import Action
from .log import Log
from .actor_state import ActorState


class Actor:
    def __init__(self, name: str):
        self.name = name
        self.abilities: List[Ability] = []
        self._state: ActorState = ActorState()

    @staticmethod
    def named(name: str):
        return Actor(name)

    @property
    def state(self):
        return self._state

    def clean_up(self):
        for ability in self.abilities:
            ability.clean_up()

    def can(self, *abilities: Ability):
        self.abilities.extend(abilities)
        return self

    who_can = can

    def ability(self, ability_type: type):
        for ability in self.abilities:
            if isinstance(ability, ability_type):
                return ability
        assert False, "Actor " + self.name + " does not have ability '" + ability_type.__name__ + "'"

    @staticmethod
    def _set_log_type_before_task_or_action(task_or_action: TaskOrAction):
        if isinstance(task_or_action, Action):
            Log.start_logging_actions()
        else:
            Log.start_logging_tasks()

    def attempts_to(self, *tasks_or_actions: TaskOrAction):
        result = None
        if len(tasks_or_actions) > 0:
            for task_or_action in tasks_or_actions:
                Actor._set_log_type_before_task_or_action(task_or_action)
                try:
                    result = task_or_action.perform_as(self)
                finally:
                    Log.end_logging_task_or_action()
        return result

    attempt_to = attempts_to

    def should(self, *conditions: Condition):
        if len(conditions) > 0:
            for condition in conditions:
                condition.check_as(self)
