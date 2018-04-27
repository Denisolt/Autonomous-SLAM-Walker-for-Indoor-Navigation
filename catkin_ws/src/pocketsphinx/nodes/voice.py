#!/usr/bin/python
import rospy
import math
import csv
import roslib
import rospy
import actionlib
from move_base_msgs.msg import *
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from std_msgs.msg import String

class VoiceControl(object):
    def __init__(self):
        rospy.on_shutdown(self.shutdown)
        """Initialize node and subscribe to necessary topics"""
        # initialize node
        rospy.init_node("command_control")
        rospy.loginfo("Done initializing pocketsphinx")
        #Movebase goal parameter
        self.goal=MoveBaseGoal()
        self.msg=Odometry()
        # subscriber to get odom and work data
        rospy.Subscriber("grammar_data", String, self.handle_output)
        rospy.spin()


    def create_marker(self,name, x, y, z, w):
        new_list = self.ReadCSVasList()
        new_list.pop(0)
        if(new_list):
            if name in new_list[0]:
                print('it already exists')
        else:
            print('Setting the marker for ' , name)
            new_list.append([name, x, y, z, w])
            self.WriteListToCSV(new_list)

    def WriteListToCSV(self, data_list):
        csv_columns = ['Name','x', 'y', 'z', 'w']
        csv_file =  "/home/walker/catkin_ws/src/ros_arduino_python/coordinates.csv"
        with open(csv_file, 'w') as csvfile:
            writer = csv.writer(csvfile, dialect='excel')
            writer.writerow(csv_columns)
            for data in data_list:
                writer.writerow(data)

    def ReadCSVasList(self):
        csv_columns = ['Name','x', 'y', 'z', 'w']
        csv_file =  "/home/walker/catkin_ws/src/ros_arduino_python/coordinates.csv"
        datalist = []
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, dialect='excel')
            datalist = list(reader)
            return datalist

    def simple_move(self,x, y, z, w):
        rospy.init_node('simple_move')
        print("initialising move")
        sac = actionlib.SimpleActionClient('move_base', MoveBaseAction)
        #set goal
        self.goal.target_pose.pose.position.x = x
        self.goal.target_pose.pose.position.y = y
        self.goal.target_pose.pose.orientation.z = z
        self.goal.target_pose.pose.orientation.w = w
        self.goal.target_pose.header.frame_id = 'map'
        self.goal.target_pose.header.stamp = rospy.Time.now()
        #start listner
        sac.wait_for_server()
        #send goal
        sac.send_goal(self.goal)
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
                self.simple_move(row[1], row[2], row[3],row[4])
            else:
                print("coordinate does not exist yet")

    def handle_output(self,data):
        """Map out grammar recognized commands in speech to terminal commands"""
        print (data.data)
        if "this is the kitchen" in data.data.lower():
            self.create_marker('Kitchen', self.msg.pose.pose.position.x, self.msg.pose.pose.position.y, self.msg.pose.pose.orientation.z, self.msg.pose.pose.orientation.w)
        elif "this is the living room" in data.data.lower():
            self.create_marker('LivingRoom', self.msg.pose.pose.position.x, self.msg.pose.pose.position.y, self.msg.pose.pose.orientation.z, self.msg.pose.pose.orientation.w)
        elif "this is the bath room" in data.data.lower():
            self.create_marker('BathRoom', self.msg.pose.pose.position.x, self.msg.pose.pose.position.y, self.msg.pose.pose.orientation.z, self.msg.pose.pose.orientation.w)
        elif "this is the dining room" in data.data.lower():
            self.create_marker('DiningRoom', self.msg.pose.pose.position.x, self.msg.pose.pose.position.y, self.msg.pose.pose.orientation.z, self.msg.pose.pose.orientation.w)
        elif "get to the kitchen" in data.data.lower():
            self.where2move('Kitchen')
        elif "get to the living room" in data.data.lower():
            self/where2move("LivingRoom")
        elif "get to the bath room" in data.data.lower():
            self.where2move('BathRoom')
        elif "get to the dining room" in data.data.lower():
            self.where2move('DiningRoom')    

    def shutdown():
        """This function is executed on node shutdown."""
        # command executed after Ctrl+C is pressed
        rospy.loginfo("Stop ASRControl")
        rospy.sleep(1)



if __name__ == "__main__":
    VoiceControl()