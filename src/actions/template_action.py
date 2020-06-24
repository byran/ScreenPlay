"""Example file containing a minimum implementation of an Action"""

from screenplay import Action, Actor, log_message


class template_action(Action):
    @log_message('Enter a description of what the action does')
    def perform_as(self, actor: Actor):
        # Use an ability the actor has, (accessed using
        # `actor.ability(ability_type)`) and interact with
        # the system under test
        pass
