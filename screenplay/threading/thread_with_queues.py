import threading
from queue import Queue
from typing import Callable, Any


class MessageWithCompleteEvent():
    def __init__(self, message):
        self._complete = threading.Event()
        self._message = message

    @property
    def complete(self) -> threading.Event:
        return self._complete

    @property
    def message(self):
        return self._message


class ThreadWithQueues:
    def __init__(self, thread_function: Callable[[Queue, Queue, Any], None], daemon=True, arg=None):
        self._to_thread_queue = Queue()
        self._from_thread_queue = Queue()
        self._thread = threading.Thread(
            target=thread_function,
            args=(self._to_thread_queue, self._from_thread_queue, arg),
            daemon=daemon
        )

    def put_message(self, message) -> threading.Event:
        m = MessageWithCompleteEvent(message)
        self._to_thread_queue.put(m)
        return m.complete

    @property
    def number_of_output_messages(self):
        return self._from_thread_queue.qsize()

    def get_message(self, block=True, timeout=None):
        return self._from_thread_queue.get(block=block, timeout=timeout)

    @property
    def to_thread_queue(self) -> Queue:
        return self._to_thread_queue

    @property
    def from_thread_queue(self) -> Queue:
        return self._from_thread_queue

    def start(self):
        self._thread.start()

    def join(self, timeout=None):
        self._thread.join(timeout=timeout)
