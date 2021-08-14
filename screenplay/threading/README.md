# Threading helper classes for Screen Play pattern

## ThreadWithQueues & MessageWithCompleteEvent

Create a function that will run on the thread that takes three arguments:

* ```in_queue``` of type ```Queue``` to receive messages from the main thread
* ```out_queue``` of type ```Queue``` to send messages to the main thread
* ```data``` of any type to receive user defined data

Pass this function to the constructor of the ```ThreadWithQueues``` class. The
```data``` parameter of the thread function can be specified by setting the
```arg``` named parameter of the constructor of ```ThreadWithQueues``` class.

```python
from thread_with_queues import ThreadWithQueues, MessageWithCompleteEvent
from queue import Queue
import time


def thread_function(in_queue: Queue, out_queue: Queue, data):
    while True:
        item: MessageWithCompleteEvent = in_queue.get()
        if item.message is None:
            # Indicate the item has been completed
            item.complete.set()
            break

        # Run operation based on message
        time.sleep(item.message)

        # Indicate the item has been completed
        item.complete.set()

        # Indicate to the Queue that the item is complete
        in_queue.task_done()


thread = ThreadWithQueues(thread_function)
thread.start()
complete_event1 = thread.put_message(5)
complete_event2 = thread.put_message(None)

complete_event1.wait()
complete_event2.wait()

thread.join()
```
