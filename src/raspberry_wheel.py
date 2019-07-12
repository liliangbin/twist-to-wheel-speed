# -*- coding: utf-8 -*-

import time

from RPi import GPIO

PWMA = 36
AIN1 = 40  # 1      0
AIN2 = 38  # 0      1
#  后退    前进
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
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
        GPIO.output(BIN1, GPIO.LOW)
        GPIO.output(BIN2, GPIO.LOW)

    # init the raspberry pin  output

    def run(self, pwmA_dc=0, pwmB_dc=0):
        # INFO 2019/7/11 21:06 liliangbin  根据占空比转化为速度

        AIN1_IN = GPIO.LOW
        AIN2_IN = GPIO.HIGH
        BIN1_IN = GPIO.LOW
        BIN2_IN = GPIO.HIGH
        # 默认是前进的方向
        if pwmA_dc < 0:
            AIN1_IN = GPIO.HIGH
            AIN2_IN = GPIO.LOW  # 后退
            pwmA_dc = -pwmA_dc
        if pwmB_dc < 0:
            BIN1_IN = GPIO.HIGH
            BIN2_IN = GPIO.LOW  # 后退
            pwmB_dc = -pwmB_dc  # 必须是一个正数

        if pwmA_dc > 80: pwmA_dc = 80
        if pwmB_dc > 80: pwmB_dc = 80
        print 'pwma==', pwmA_dc, '   pwmb=', pwmB_dc
        self.pwmA_dc = pwmA_dc
        self.pwmB_dc = pwmB_dc
        self.pwmA.ChangeDutyCycle(self.pwmA_dc)
        self.pwmB.ChangeDutyCycle(self.pwmB_dc)

        GPIO.output(AIN1, AIN1_IN)
        GPIO.output(AIN2, AIN2_IN)
        GPIO.output(BIN1, BIN1_IN)
        GPIO.output(BIN2, BIN2_IN)
        GPIO.output(PWMA, GPIO.HIGH)
        GPIO.output(PWMB, GPIO.HIGH)
        time.sleep(0.3)

    def stop(self):
        self.pwmA.stop()
        self.pwmB.stop()
        GPIO.cleanup()


if __name__ == '__main__':
    raspberry = Raspberry()
    raspberry.run(pwmA_dc=40, pwmB_dc=40)

    time.sleep(3)
    raspberry.stop()
