#!/usr/bin/env python3

import rospy
import assignment_2_2022.msg
import os
import sys

from std_srvs.srv import Empty,EmptyResponse

Number_goals_reached =0
Number_goals_canceled = 0
seq =1 
start = 1

# callback function for service server
# prints the number of goals reached and canceled when called
# returns an empty response
# this function is called when the service is called
def service_callback(req):
    global Number_goals_reached , Number_goals_canceled , seq
    print("*************************************************************************")
    print(f"Seq: {seq}")
    print(f"Number of goals reached: {Number_goals_reached}")
    print(f"Number of goals canceled: {Number_goals_canceled}")
    print("\n*************************************************************************") 
    seq += 1
    return EmptyResponse() 

# callback function for subscriber
# increments the number of goals reached or canceled when a goal is reached or canceled
# this function is called when a message is received
# @param data: the message received
# @type data: assignment_2_2022.msg.PlanningActionResult
# @return: None
def subscriber_callback(data):
    if data.status.status == 2:         # 2 is the status for canceled 
        global Number_goals_canceled
        Number_goals_canceled += 1
    elif data.status.status == 3:       # 3 is the status for reached
        global Number_goals_reached
        Number_goals_reached += 1

# menu function 
# it prints the menu containing what the node does
#@param start: a variable that is used to print the menu only once
#@type start: int
#@return: None
def menu(start):
    if start == 1:
        os.system('clear')
        print("\n*************************************************************************")
        print(" B.\n     This node is a service node that, when called,")
        print("     prints the number of goals reached and cancelled")
        print("*************************************************************************\n") 
        start = 0    

# main function
# initializes the node, creates a subscriber and a service server
if __name__ == "__main__":
    try:
        menu(start) # prints the menu
        rospy.init_node('b_goal_status') # initializes the node named b_goal_status
        rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, subscriber_callback) # creates a subscriber to the topic /reaching_goal/result 
        rospy.Service('goal_status', Empty, service_callback)   # creates a service server named goal_status 
        rospy.spin() # keeps the node running
    # if the node is interrupted, print an error message to the user
    except rospy.ROSInterruptException:
        print("program interrupted before completion", file=sys.stderr)
