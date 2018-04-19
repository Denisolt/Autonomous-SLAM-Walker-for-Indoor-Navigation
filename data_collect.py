import roslib
import rospy
import geometry_msgs.msg
from nav_msgs.msg import Odometry
import pandas as pd
import os
import time
global df2
global new
global df
import datetime

def collecter(msg):
	df = pd.DataFrame.from_csv("~/catkin_ws/data/"+str(name)+".csv")
	df2 = pd.DataFrame({'time':[datetime.datetime.now()], 'pos-x':[msg.pose.pose.position.x], 'pos-y': [msg.pose.pose.position.y], 'pos-z':[msg.pose.pose.position.z],
		'ori-x':[msg.pose.pose.orientation.x],'ori-y':[msg.pose.pose.orientation.y],'ori-z':[msg.pose.pose.orientation.z],'ori-w':[msg.pose.pose.orientation.w]})
	new = pd.concat([df,df2])
	new.to_csv("~/catkin_ws/data/"+str(name)+".csv", header=True, columns=['time','pos-x','pos-y','pos-z','ori-x','ori-y','ori-z', 'ori-w'])

name = raw_input("How do you want to call this? ")
path = "~/catkin_ws/data/"+str(name)+".csv"
start = pd.DataFrame(columns=['time','pos-x','pos-y','pos-z','ori-x','ori-y','ori-z', 'ori-w'])
start.to_csv("~/catkin_ws/data/"+str(name)+".csv")
rospy.init_node('check_odometry')
cont_bool = True
while cont_bool:
	odom_sub = rospy.Subscriber('/odom', Odometry, collecter)
	time.sleep(250)
rospy.spin()