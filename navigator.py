#!/usr/bin/env python

import roslib;
import rospy
import actionlib
import sys
#move_base_msgs
from move_base_msgs.msg import *

def simple_move():

    rospy.init_node('simple_move')

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()


    #set goal
    goal.target_pose.pose.position.x = sys.argv[0]
    goal.target_pose.pose.position.y = sys.argv[1]

    goal.target_pose.pose.orientation.z = sys.argv[2]
    goal.target_pose.pose.orientation.w = sys.argv[3]
    
    goal.target_pose.header.frame_id = 'first_move'
    goal.target_pose.header.stamp = rospy.Time.now()

    #start listner
    sac.wait_for_server()

    #send goal
    sac.send_goal(goal)

    #finish
    sac.wait_for_result()

    #print result
    print sac.get_result()


if __name__ == '__main__':
    try:
        simple_move()
    except rospy.ROSInterruptException:
        print "Keyboard Interrupt"