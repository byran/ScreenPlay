from screenplay import Actor, Ability, Action, Question, Task
from screenplay.matcher import Matcher
from screenplay.task_or_action import TaskOrAction

actor = Actor.named('unused')

Ability().clean_up()
Action().perform_as(actor)
Question().answered_by(actor)
Task().perform_as(actor)

Matcher().matches(2)
message = Matcher().fail_message

TaskOrAction().perform_as(actor)
