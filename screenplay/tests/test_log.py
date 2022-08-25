from screenplay import Actor, Task, Action, log_message, action_log_message
from screenplay.log import Log, _LogIndent
from .stub_function_task import stub_function_task
from .stub_function_action import stub_function_action
from .fixture_log_capture import log_capture


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


def test_The_log_indent_is_increased_for_a_function_Task():
    user = Actor('user')

    Log.to_actions()
    original_indent = _LogIndent.current_indent
    task_indent = 0

    def function_task():
        @log_message('function task')
        def task(actor):
            nonlocal task_indent
            task_indent = _LogIndent.current_indent
        return task

    try:
        user.attempts_to(
            function_task()
        )
    except AssertionError:
        pass

    assert ((task_indent - original_indent) == 2), 'The indent was not set for a function task'


def test_The_log_indent_is_increased_for_a_function_Action_when_logging_to_actions():
    user = Actor('user')

    Log.to_actions()
    original_indent = _LogIndent.current_indent
    task_indent = 0
    action_indent = 0

    def function_action():
        @action_log_message('function action')
        def action(actor):
            nonlocal action_indent
            action_indent = _LogIndent.current_indent
        return action

    def function_task():
        @log_message('function task')
        def task(actor: Actor):
            nonlocal task_indent
            task_indent = _LogIndent.current_indent
            actor.attempts_to(
                function_action()
            )
        return task

    try:
        user.attempts_to(
            function_task()
        )
    except AssertionError:
        pass

    assert ((task_indent - original_indent) == 2), 'The indent was not set for a function task'
    assert ((action_indent - original_indent) == 4), 'The indent was not set for a function action'


def test_The_log_indent_is_increased_for_a_function_Action_when_logging_to_actions():
    user = Actor('user')

    Log.to_tasks()
    original_indent = _LogIndent.current_indent
    task_indent = 0
    action_indent = 0

    def function_action():
        @action_log_message('function action')
        def action(actor):
            nonlocal action_indent
            action_indent = _LogIndent.current_indent
        return action

    def function_task():
        @log_message('function task')
        def task(actor: Actor):
            nonlocal task_indent
            task_indent = _LogIndent.current_indent
            actor.attempts_to(
                function_action()
            )
        return task

    try:
        user.attempts_to(
            function_task()
        )
    except AssertionError:
        pass

    assert ((task_indent - original_indent) == 2), 'The indent was not set for a function task'
    assert ((action_indent - original_indent) == 2), 'The indent was increased for a function action when logging to tasks'


def test_Task_messages_are_output_by_the_log(log_capture):
    Log.to_tasks()

    bob = Actor.named('Bob')
    bob.attempts_to(
        stub_function_task('Do something')
    )

    assert len(log_capture) == 1
    assert log_capture[0][0] == '    '
    assert log_capture[0][1] == 'Do something'


def test_Action_messages_are_output_by_the_log(log_capture):

    @log_message('function task')
    def task(actor: Actor):
        actor.attempts_to(
            stub_function_action('Do something fine grain')
        )

    Log.to_actions()

    bob = Actor.named('Bob')
    bob.attempts_to(
        task
    )

    assert len(log_capture) == 2
    assert log_capture[1][0] == '      '
    assert log_capture[1][1] == 'Do something fine grain'


def test_Action_messages_are_not_output_by_the_log_when_logging_to_tasks(log_capture):

    @log_message('function task')
    def task(actor: Actor):
        actor.attempts_to(
            stub_function_action('Do something fine grain')
        )

    Log.to_tasks()

    bob = Actor.named('Bob')
    bob.attempts_to(
        task
    )

    assert len(log_capture) == 1
    assert log_capture[0][0] == '    '
    assert log_capture[0][1] == 'function task'
