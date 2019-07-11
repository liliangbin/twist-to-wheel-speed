import time

import RPi.GPIO as gpio

pin = 33
pin_wheel = 35
while True:
    print 'go straight '
    gpio.setmode(gpio.BOARD)
    gpio.setup(pin, gpio.OUT)
    gpio.setup(pin_wheel, gpio.OUT)
    gpio.output(pin_wheel, gpio.HIGH)
    p = gpio.PWM(pin, 400)
    p.start(0)
    dc = 10
    for i in range(40):
        dc += 2
        print 'dc:', dc
        p.ChangeDutyCycle(dc)
        time.sleep(0.3);
    p.stop()
    gpio.cleanup()
    print 'done'
