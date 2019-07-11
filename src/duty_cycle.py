class DutyCycle(object):
    def __init__(self):
        self.left_vel = 0
        self.right_vel = 0
        self.wheel_dist = 0.32  # m 对应轮子的轴距
        pass

    def twist_to_wheel(self, msg):
        pass

    def calculate_pub(self, msg):
        print type(msg.linear.x)
        print msg.linear.x + 'linear x ' + msg.angular.z + ' angular z ' + '\n'
        self.left_vel = msg.linear.x - msg.angular.z * self.wheel_dist / 2
        self.right_vel = msg.linear.x - msg.angular.z * self.wheel_dist / 2
        # INFO 2019/7/11 22:21 liliangbin  初期设想，直接给一个相关的百分比值。然后最好用上pid算法  。。。

