#! /usr/bin/env python

import rospy

rospy.init_node("node_three")
rate = rospy.Rate(2)               
while not rospy.is_shutdown():     
   print "launch node is in active mode"
   rate.sleep()