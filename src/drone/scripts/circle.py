#!/usr/bin/env python3

import rospy
import sys
import math
from drone.srv import PoseCommander

rospy.init_node("commander", anonymous=True)


def pose_command(x,y):
    commander=rospy.ServiceProxy("pose_commander", PoseCommander)
    commander.call(x,y,5)

def draw_circle( radius):
    num_of_pieces = 100
    vector = [0,0]
    vectors = []
    for i in range(num_of_pieces):
        vectors.append(vector)
    
    vectors[0][0]=0
    vectors[0][1]=radius
    angle = (360/num_of_pieces)*0.0174532925 #radians 
    
    for i in range(1,num_of_pieces):
        vectors[i][0] = vectors[i-1][0]*math.cos(angle) - vectors[i-1][1]*math.sin(angle)
        vectors[i][1] = vectors[i-1][1]*math.cos(angle) + vectors[i-1][0]*math.sin(angle)
        pose_command(vectors[i][0], vectors[i][1])
        rospy.sleep(0.5)

if __name__ == "__main__":
    
    r = float(sys.argv[1])
    draw_circle(r)
    