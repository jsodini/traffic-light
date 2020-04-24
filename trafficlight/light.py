import enum

import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


class Light:

    def __init__(self, pin: int) -> None:
        self._pin = pin
        self.prepare()

    def prepare(self) ->None:
        GPIO.setup(self._pin, GPIO.OUT)

    def activate(self) -> None:
        GPIO.output(self._pin, GPIO.HIGH)

    def deactivate(self) -> None:
        GPIO.output(self._pin, GPIO.LOW)


class Lights(enum.Enum):

    GREEN = Light(26)
    YELLOW = Light(13)
    RED = Light(19)

    
if __name__ == '__main__':
    Lights.GREEN.value.deactivate()
    Lights.YELLOW.value.deactivate()
    Lights.RED.value.deactivate()
