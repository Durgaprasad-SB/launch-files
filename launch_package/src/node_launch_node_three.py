#! /usr/bin/env python

import rospy

rospy.init_node("node_four")
rate = rospy.Rate(2)               
while not rospy.is_shutdown():     
   print "node four is also in active mode"
   rate.sleep()