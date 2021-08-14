from screenplay import Action, Actor, log_message
import time


class pause_for(Action):
    def __init__(self, time: float):
        super().__init__()
        self._time = time

    def seconds(self):
        return self

    def milliseconds(self):
        self._time /= 1000
        return self

    @log_message('Pausing for {self._time} seconds')
    def perform_as(self, actor: Actor):
        time.sleep(self._time)
