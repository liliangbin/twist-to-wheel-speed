# -*- coding: utf-8 -*-

import time

from RPi import GPIO

PWMA = 36
AIN1 = 40
AIN2 = 38

PWMB = 33
BIN1 = 37
BIN2 = 35


class Raspberry(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(PWMA, GPIO.OUT)
        GPIO.setup(AIN1, GPIO.OUT)
        GPIO.setup(AIN2, GPIO.OUT)

        GPIO.setup(PWMB, GPIO.OUT)
        GPIO.setup(BIN1, GPIO.OUT)
        GPIO.setup(BIN2, GPIO.OUT)

        self.pwmA = GPIO.PWM(PWMA, 400)
        self.pwmA_dc = 0
        self.pwmA.start(self.pwmA_dc)
        self.pwmB = GPIO.PWM(PWMB, 400)
        self.pwmB_dc = 0
        self.pwmB.start(self.pwmB_dc)
        # init duty_cycle
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.HIGH)
        GPIO.output(BIN2, GPIO.LOW)

    # init the raspberry pin  output

    def run(self, pwmA_dc, pwmB_dc, AIN1_IN=GPIO.HIGH, AIN2_IN=GPIO.LOW, BIN1_IN=GPIO.HIGH, BIN2_IN=GPIO.LOW):
        # INFO 2019/7/11 21:06 liliangbin  根据占空比转化为速度
        self.pwmA_dc = pwmA_dc
        self.pwmB_dc = pwmB_dc
        self.pwmA.ChangeDutyCycle(self.pwmA_dc)
        self.pwmB.ChangeDutyCycle(self.pwmB_dc)

        GPIO.output(AIN1, AIN1_IN)
        GPIO.output(AIN2, AIN2_IN)
        GPIO.output(BIN1, BIN1_IN)
        GPIO.output(BIN2, BIN2_IN)
        time.sleep(0.3)

    def stop(self):
        self.pwmA.stop()
        self.pwmB.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    pass
