import rospy
from ros_arduino_python.arduino_driver import Arduino
from ros_arduino_python.arduino_sensors import *
from ros_arduino_msgs.srv import *
from ros_arduino_python.base_controller import BaseController
from geometry_msgs.msg import Twist
import os, time
import thread
from serial.serialutil import SerialException

if __name__ == "__main__":

    portName = "/dev/ttyACM0"

    baudRate = 57600

    myArduino = Arduino(port=portName, baudrate=baudRate, timeout=0.5)
    myArduino.connect()

    print "Sleeping for 1 second..."
    time.sleep(1)

    time_start=time.time()
    while True:
        time_now = time.time()
        if time_now - time_start > 10:
            break
        else:
            tester=myArduino.get_encoder_counts()

    #print "Current encoder counts", myArduino.encoders()

    print "Connection test successful.",

    myArduino.stop()
    myArduino.close()

    print "Shutting down Arduino."
