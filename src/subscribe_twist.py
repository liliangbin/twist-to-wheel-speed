# -*- coding: utf-8 -*-

import rospy
from geometry_msgs import Twist  # velocity


def callback(msg):
    # INFO 2019/7/11 20:09 liliangbin  设置树莓派引脚的输出 。

    pass


rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('cmd_vel', Twist, callback)

rospy.spin()
