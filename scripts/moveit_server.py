#!/usr/bin/env python

import rospy
from moveit_commander import MoveGroupCommander
from sensor_msgs.msg import JointState
from geometry_msgs.msg import Pose

group = MoveGroupCommander("right_arm") # arm for fetch
group.set_end_effector_link('r_gripper_tool_frame')
group.set_pose_reference_frame('/base_footprint')

def pose_callback(pose):
    pos = pose.position
    qtr = pose.orientation
    if qtr.x == 0 and qtr.y == 0 and qtr.z == 0 and qtr.w == 0:
        group.set_position_target([pos.x, pos.y, pos.z])
    else: group.set_pose_target(pose)
    group.go()

def joint_callback(msg):
    goal = map(lambda joint_name: msg.position[msg.name.index(joint_name)],
               group.get_active_joints())
    group.set_joint_value_target(goal)
    group.go()

if __name__ == "__main__":
    rospy.init_node('movescratch')
    rospy.Subscriber("movescratch/pose_goal", Pose, pose_callback)
    rospy.Subscriber("movescratch/joint_goal", JointState, joint_callback)
    rospy.spin()
