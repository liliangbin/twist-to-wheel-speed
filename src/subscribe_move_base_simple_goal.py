#!/usr/bin/python

import MySQLdb
import rospy
from geometry_msgs import PoseStamped  # velocity


# back function
def callback(msg):
    print msg.pose.position.x
    print msg.pose.orientation.x
    print 'get pose  and prepar to saving in databases '
    location = input('location === ')

    # 放入数据库

    # TODO 2019/7/8 19:32 liliangbin 加入数据库
    join_data_bases(msg, location)
    # INFO 2019/7/8 19:33   加入数据库


def join_data_bases(msg, location):
    database = MySQLdb.connect(host="forcebing.top", port=3306, user="llb", passwd="123456",
                               db="liliangbin")
    database.set_character_set('utf8')
    cursor = database.cursor()
    query = """INSERT INTO  move_base_goal(position_x,position_y,position_z,orientation_x,orientation_y,orientation_z,orientation_w,location) VALUES (%s, %s, %s, %s,%s, %s, %s, %s)"""

    values = (
        msg.pose.position.x,
        msg.pose.position.y,
        msg.pose.position.z,
        msg.pose.orientation.x,
        msg.pose.orientation.y,
        msg.pose.orientation.z,
        msg.pose.orientation.w,
        location)
    print(values)

    cursor.exect(query, values)
    cursor.close()
    database.commit()
    database.close()



rospy.init_node('topic_subscriber')

sub = rospy.Subscriber('move_base_simple/goal', PoseStamped, callback)

rospy.spin()
