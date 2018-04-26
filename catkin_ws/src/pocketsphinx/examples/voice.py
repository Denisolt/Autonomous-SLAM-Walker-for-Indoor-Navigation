#!/usr/bin/python
import rospy

import math
import csv
import roslib
import rospy
import actionlib
from move_base_msgs.msg import *
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Pose
from std_msgs.msg import String

# Movebase goal var
goal=MoveBaseGoal() 

def create_marker(self,name, x, y, z, w):
    new_list = self.ReadCSVasList()
    new_list.pop(0)
    if name in new_list[0]:
        print('it already exists')
    else:
        print('Setting the marker for ' , name)
        new_list.append([name, x, y, z, w])
        self.WriteListToCSV(new_list)

def WriteListToCSV(self, data_list):
    csv_columns = ['Name','x', 'y', 'z']
    csv_file =  "/home/walker/Desktop/coordinates.csv"
    with open(csv_file, 'w') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(csv_columns)
        for data in data_list:
            writer.writerow(data)

def ReadCSVasList(self):
    csv_columns = ['Name','x', 'y', 'z', 'w']
    csv_file =  "/home/walker/Desktop/coordinates.csv"
    datalist = []
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, dialect='excel')
        datalist = list(reader)
        return datalist


def simple_move(self,x, y, z):
    rospy.init_node('simple_move')
    sac = actionlib.SimpleActionClient('move_base')

    #set goal
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    goal.target_pose.pose.orientation.z = z
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


def where2move(self, coordinate):
    new_list = self.ReadCSVasList()
    new_list.pop(0)
    for row in new_list:
        if row[0] == coordinate:
            print("moving to :",row[1], row[2], row[3], row[4])
            self.simple_move(row[1], row[2], row[3])
        else:
            print("coordinate does not exist yet")

def handle_output(data):
    """Map out grammar recognized commands in speech to terminal commands"""
    print (data.data)
    if "this is the kitchen" in data.data.lower():
        self.create_marker('Kitchen', msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    elif "this is the living room" in data.data.lower():
        self.create_marker('LivingRoom', msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    elif "this is the bath room" in data.data.lower():
        self.create_marker('BathRoom', msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    elif "this is the dining room" in data.data.lower():
        self.create_marker('DiningRoom', msg.pose.pose.position.x, msg.pose.pose.position.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)
    elif "go to the kitchen" in data.data.lower():
        self.where2move('Kitchen')
    elif "go to the living room" in data.data.lower():
        self/where2move("LivingRoom")
    elif "go to the bath room" in data.data.lower():
        self.where2move('BathRoom')
    elif "go to the dining room" in data.data.lower():
        self.where2move('DiningRoom')    

def shutdown():
    """This function is executed on node shutdown."""
    # command executed after Ctrl+C is pressed
    rospy.loginfo("Stop ASRControl")
    rospy.sleep(1)

def init():
    """Initialize node and subscribe to necessary topics"""
    # initialize node
    rospy.init_node("command_control")
    # Call custom function on node shutdown
    rospy.on_shutdown(shutdown)
    odom_sub = rospy.Subscriber('/odom', Odometry, collecter)
    rospy.Subscriber("grammar_data", String, handle_output)
    rospy.spin()

if __name__ == "__main__":
    init()
