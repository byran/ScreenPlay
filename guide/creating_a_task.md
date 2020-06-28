# Creating a task

## Creating a new task file

### 1. Create a file for the task

Create a new file in the ```src/tasks``` directory and name it the same as the
task you're going to create. The name should describe what the task is going to
do and should read like part of a sentance. The name should be all lower case
(unless the case is indicating a specific value) and have words separated with
an underscore ( ```_``` ).

### 2. Copy the template_task for an easy start point

Copy the contents of the ```src/tasks/template_task.py``` file (shown below)
into your new file for an easy start point. Update or remove the docstring at
the top of the file.

```python
"""Example file containing a minimum implementation of a Task"""

from screenplay import Task, Actor, log_message


class template_task(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # A parameter list of Action objects
        )
```

### 3. Name the class to the name of the task

Name the class the name of the task (i.e. the same as the filename without the extension)

```python
from screenplay import Task, Actor, log_message


class search_for_Hello_world(Task):
    @log_message('Enter a description of what the task does')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            # A parameter list of Action objects
        )
```

### 4. Update the log message

### 5. Import Actions and make the actor perform them

### 6. Accepting parameters in the constructor

### 7. Accepting parameters in other methods

### 8. Including parameters in the log message

### 9. Using the Actors state to store information *** Does this want to be here? ***

## A completed Task file

``` python
from screenplay import Task, Actor, log_message
from actions_selenium import enter_text, send_enter_key_to
from pages.google_homepage import google_homepage


class search_for(Task):
    def __init__(self, text: str):
        super().__init__()
        self._text = text

    @log_message('Enter \'{self._text}\' into google')
    def perform_as(self, actor: Actor):
        actor.attempts_to(
            enter_text(self._text).into_element(google_homepage.search_textbox),
            send_enter_key_to().element(google_homepage.search_textbox)
        )
```
