# -*- coding: utf-8 -*-

import rospy
from geometry_msgs.msg import Twist  # velocity

from duty_cycle import DutyCycle
from raspberry_wheel import Raspberry

cycle = DutyCycle()

raspberry = Raspberry()


def callback(msg):
    # INFO 2019/7/11 20:09 liliangbin  设置树莓派引脚的输出 。
    print 'msg.linear.x==>', msg.linear.x, 'z==>', msg.angular.z, '\n'

    left_dc, right_dc = cycle.calculate_pub(msg)
    raspberry.run(left_dc, right_dc)


try:

    rospy.init_node('topic_subscriber')

    sub = rospy.Subscriber('cmd_vel', Twist, callback)

    rospy.spin()

except KeyboardInterrupt:

    raspberry.stop()
