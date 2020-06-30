# ```actions_common``` built in Actions

## Actions for accessing/checking ```Actor```'s state

### actions_common.if_value_of

The ```if_value_of``` action will run a list of ```Task```s and/or
```Action```s if the value of an element of the ```Actor```'s state matches the
specified value(s).

*** TODO: Add more detail here ***

```python
from actions_common import if_value_of, fail_with_message

@step('...')
def step_impl(context):
    context.they.attempts_to(
        if_value_of('ok_button').is_None().then(
            fail_with_message('Unable to find the "OK" button')
        )
    )
```

### actions_common.select_element_at_index

## Actions for slowing and failing tests

### actions_common.fail_with_message

The ```fail_with_message``` actions will cause the scenario/test to fail when
the actions is run. It's takes a single constructor parameter, the failure
message.

```python
from actions_common import fail_with_message

@step('...')
def step_impl(context):
    context.they.attempts_to(
        fail_with_message('Failure message')
    )
```

### actions_common.pause_for

Pauses the execution of the test/scenario for the specified amount of time. The
action takes one constructor parameter, the time (in seconds by default).

The ```pause_for``` action has two methods that modify it's behaviour:

* ```seconds()``` - specifies the time is in seconds. Although this call is
  optional (as the time is in seconds by default), it is recommended.
* ```milliseconds()``` - specifies the time is in milliseconds instead of
  seconds.

```python
from actions_common import pause_for

@step('...')
def step_impl(context):
    context.they.attempts_to(
        pause_for(2).seconds(),
        pause_for(100).milliseconds()
    )
```
