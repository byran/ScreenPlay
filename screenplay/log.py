import functools


class _LogIndent:
    indent_size = 2
    current_indent = indent_size * 2

    @classmethod
    def increase_indent(cls):
        cls.current_indent = cls.current_indent + cls.indent_size

    @classmethod
    def decrease_indent(cls):
        if cls.current_indent > cls.indent_size:
            cls.current_indent = cls.current_indent - cls.indent_size

    @classmethod
    def indent(cls) -> str:
        return ' ' * cls.current_indent


class Log:
    _output_messages_to_level = 0
    _current_level = 0
    _previous_levels = []
    current_actor = None
    write_line = print

    task_log_level = 1
    action_log_level = 2

    @classmethod
    def to_actions(cls):
        cls._output_messages_to_level = cls.action_log_level

    @classmethod
    def to_tasks(cls):
        cls._output_messages_to_level = cls.task_log_level

    @classmethod
    def start_logging_actions(cls):
        cls._previous_levels.append(cls._current_level)
        cls._current_level = cls.action_log_level
        if cls.should_log():
            _LogIndent.increase_indent()

    @classmethod
    def start_logging_tasks(cls):
        cls._previous_levels.append(cls._current_level)
        cls._current_level = cls.task_log_level
        if cls.should_log():
            _LogIndent.increase_indent()

    @classmethod
    def end_logging_task_or_action(cls):
        if len(cls._previous_levels) > 0:
            cls._current_level = cls._previous_levels.pop()
            if cls.should_log():
                _LogIndent.decrease_indent()

    @classmethod
    def should_log(cls):
        return cls._current_level <= cls._output_messages_to_level


def log_message(message: str):
    def decorator_log_message(func):
        @functools.wraps(func)
        def wrapper_log_message(*args, **kwargs):
            if Log.should_log():
                Log.write_line(_LogIndent.indent(), message.format(self=args[0]), sep='')
            value = func(*args, **kwargs)
            return value
        return wrapper_log_message
    return decorator_log_message


def action_log_message(message: str):
    def decorator_log_message(func):
        @functools.wraps(func)
        def wrapper_log_message(*args, **kwargs):
            if Log.should_log():
                Log.write_line(_LogIndent.indent(), message.format(self=args[0]), sep='')
            value = func(*args, **kwargs)
            return value
        wrapper_log_message.is_screenplay_action = True
        return wrapper_log_message
    return decorator_log_message
