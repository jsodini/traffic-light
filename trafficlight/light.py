import RPi.GPIO as GPIO


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


if __name__ == '__main__':
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    green = Light(26)
    yellow = Light(19)
    red = Light(13)

    import time
    while True:
        green.activate()
        time.sleep(0.5)
        yellow.activate()
        time.sleep(0.5)
        green.deactivate()
        time.sleep(0.5)
        red.activate()
        time.sleep(0.5)
        yellow.deactivate()
        time.sleep(2)

