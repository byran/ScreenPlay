from screenplay import Actor, Task, Action, log_message
from screenplay.log import Log, _LogIndent


class failing_task(Task):
    @log_message('always fails')
    def perform_as(self, actor: Actor):
        assert False, 'failing'


def test_The_log_indent_is_restored_if_a_test_fails():
    user = Actor('user')

    Log.to_actions()
    original_indent = _LogIndent.current_indent

    try:
        user.attempts_to(
            failing_task()
        )
    except AssertionError:
        pass

    assert original_indent == _LogIndent.current_indent, 'The indent was not reset if an action fails'


class record_log_indent_task(Task):
    def __init__(self, *actions):
        super().__init__()
        self.actions = actions
        self.indent = -1

    def perform_as(self, actor: Actor):
        self.indent = _LogIndent.current_indent
        actor.attempts_to(*self.actions)


class record_log_indent_action(Action):
    def __init__(self, *actions):
        super().__init__()
        self.actions = actions
        self.indent = -1

    def perform_as(self, actor: Actor):
        self.indent = _LogIndent.current_indent
        actor.attempts_to(*self.actions)


def test_The_log_indent_is_not_increased_by_actions_if_only_logging_to_tasks():
    user = Actor('user')

    Log.to_tasks()

    start_indent = _LogIndent.current_indent

    action = record_log_indent_action()
    task = record_log_indent_task(action)

    user.attempts_to(task)

    assert task.indent == start_indent + 2, 'Task not indented correctly'
    assert action.indent == start_indent + 2, 'Action not indented correctly'
