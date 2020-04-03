from screenplay import Ability
import serial

class control_led(Ability):
    def __init__(self):
        self.serialConnection = serial.Serial("COM6", 115200)

    def clean_up(self):
        pass

    def led_on(self):
        self.serialConnection.write(b"$ledon\r")

    def led_off(self):
        self.serialConnection.write(b"$ledoff\r")

def leds_for(actor):
    return actor.ability(control_led)
