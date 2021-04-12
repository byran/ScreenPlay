"""Example file containing a minimum implementation of a Question"""

from screenplay import Actor, Question


class the_search_result_titles(Question):
    def answered_by(self, actor: Actor):
        # Use an ability the actor has, (accessed using
        # `actor.ability(ability_type)`) to read from
        # the system under test and return a value to check
        return 0
