from screenplay import Action, Actor, log_message
from abilities.control_led import leds_for


class turn_led_on(Action):
    @log_message('Turns LED on')
    def perform_as(self, actor: Actor):
        leds_for(actor).led_on()
        pass
