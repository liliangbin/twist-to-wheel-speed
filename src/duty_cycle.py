# -*- coding: utf-8 -*-

TURN_CYCLE_RADIO = 200


class DutyCycle(object):
    def __init__(self):
        self.left_vel = 0
        self.right_vel = 0
        self.wheel_dist = 0.26  # m 对应轮子的轴距
        self.left_dc = 0
        self.right_dc = 0

    def twist_to_wheel(self, msg):
        pass

    def calculate_pub(self, msg):
        self.left_vel = msg.linear.x - msg.angular.z * self.wheel_dist / 2
        self.right_vel = msg.linear.x + msg.angular.z * self.wheel_dist / 2
        # INFO 2019/7/11 22:21 liliangbin  初期设想，直接给一个相关的百分比值。然后最好用上pid算法  。。。
        self.left_dc = self.left_vel * TURN_CYCLE_RADIO
        self.right_dc = self.right_vel * TURN_CYCLE_RADIO

        print 'left dc ===', self.left_dc, '   right dc ===', self.right_dc
        return self.left_dc, self.right_dc
