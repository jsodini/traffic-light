import time

import trafficlight.light as trafficlight


LIGHTS = [
    trafficlight.Lights.GREEN.value,
    trafficlight.Lights.YELLOW.value,
    trafficlight.Lights.RED.value,
]

DELAY = 0.5


def all_off():
    map(lambda x: x.deactivate(), LIGHTS)

def all_on():
    map(lambda x: x.activate(), LIGHTS)


def demo_individual_flash():
    for light in LIGHTS:
        light.activate()
        time.sleep(DELAY)
        light.deactivate()
        time.sleep(DELAY)

def demo_flash_all():
    all_on()
    time.sleep(DELAY)
    all_off()

def demo_funk_flash():
    LIGHTS[0].activate()
    LIGHTS[-1].activate()
    time.sleep(DELAY)
    LIGHTS[0].deactivate()
    lights[1].activate()
    LIGHTS[2].deactivate()

def demo():
    for _ in range(10):
        demo_individual_flash()
        demo_flash_all()
    
    for _ in range(4):
        demo_funk_flash()
    
    all_off()


if __name__ == '__main__':
    all_off()

    try:
        while True:
            demo()
    except KeyboardInterrupt:
        print("Cleaning Up")
    finally:
        all_off()
