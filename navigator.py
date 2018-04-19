#!/usr/bin/env python

import roslib;
import rospy
import actionlib
import sys
#move_base_msgs
from move_base_msgs.msg import *

def simple_move():

    initial_pose = Pose()
    pose.position.x = 0.0
    pose.position.y = 0.0
    pose.orientation.z = 0.0
    pose.orientation.w = 0.0

    rospy.init_node('simple_move')

    #Simple Action Client
    sac = actionlib.SimpleActionClient('move_base', MoveBaseAction )

    #create goal
    goal = MoveBaseGoal()


    #set goal
    goal.target_pose.pose.position.x = 1
    goal.target_pose.pose.position.y = 0

    goal.target_pose.pose.orientation.z = 0
    goal.target_pose.pose.orientation.w = 1
    
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