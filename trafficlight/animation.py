import time

import light as lightboard


LIGHTS = [
    lightboard.Lights.GREEN.value,
    lightboard.Lights.YELLOW.value,
    lightboard.Lights.RED.value,
]

DELAY = 0.25


def all_off():
    [light.deactivate() for light in LIGHTS]

def all_on():
    [light.activate() for light in LIGHTS]


def demo_individual_flash():
    for light in LIGHTS:
        light.activate()
        time.sleep(DELAY)
        light.deactivate()
        time.sleep(DELAY)


def demo_flash_all():
    all_off()
    time.sleep(DELAY)
    all_on()
    time.sleep(DELAY)
    all_off()


def demo_crawl_down():
    all_off()
    
    for light in reversed(LIGHTS):
        light.activate()
        time.sleep(DELAY)
    
    for light in reversed(LIGHTS):
        light.deactivate()
        time.sleep(DELAY)

    all_off()


def demo_funk_flash():
    all_off()
    LIGHTS[0].activate()
    LIGHTS[1].deactivate()
    LIGHTS[2].activate()
    time.sleep(DELAY)
    LIGHTS[0].deactivate()
    LIGHTS[1].activate()
    LIGHTS[2].deactivate()
    time.sleep(DELAY)
    all_off()


def demo():
    for _ in range(5):
        demo_flash_all()

    time.sleep(4 * DELAY)

    for _ in range(10):
        demo_individual_flash()
        demo_crawl_down()
        demo_funk_flash()
        demo_funk_flash()
        all_off()
        time.sleep(DELAY)
   
    for _ in range(2):
        all_on()
        time.sleep(DELAY * 2)
        all_off()
        time.sleep(DELAY * 2)

    all_off()


if __name__ == '__main__':
    all_off()

    try:
        while True:
            demo()
    except KeyboardInterrupt:
        print("Cancelling")
    finally:
        all_off()

