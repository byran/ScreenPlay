import pytest
from screenplay.log import Log


@pytest.fixture
def log_capture():
    original_write_line = Log.write_line
    messages = []

    def recorded_write_line(*values: object, sep: str = None):
        messages.append(values)

    Log.write_line = recorded_write_line

    yield messages

    Log.write_line = original_write_line
