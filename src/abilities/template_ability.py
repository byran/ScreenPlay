"""Example file containing a minimum implementation of an Ability"""

from screenplay import Ability


class template_ability(Ability):
    def clean_up(self):
        # clean up any objects or external state that was set by the
        # Ability during the test run
        pass
