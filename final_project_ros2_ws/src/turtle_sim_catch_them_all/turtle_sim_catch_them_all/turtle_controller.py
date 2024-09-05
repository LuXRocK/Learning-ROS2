#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist

class TurtleControllerNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("turtle_controller") #CHANGE NAME

        self.target_x = 9.0
        self.target_y = 7.0
        
        self.pose_ = None

        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_Turtle_Position, 10)

        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.get_logger().info("Turtle controller node has been started")

    def callback_Turtle_Position(self, msg):
        self.pose_ = msg

    def control_loop(self):
        if self.pose_ == None:
            return
        distance_x = self.target_x - self.pose_.x
        distance_y = self.target_y - self.pose_.y
        distance = math.sqrt((distance_x*distance_x) + (distance_y*distance_y))

        msg = Twist()
        
        if distance > 0.5:
            #position
            msg.linear.x = 2*distance
            
            #orientation
            goal_theta = math.atan2(distance_y, distance_x)
            diff_ang = goal_theta - self.pose_.theta
            
            #normalize diff (idk what's going on)
            if diff_ang > math.pi:
                diff_ang -= 2*math.pi
            elif diff_ang < -math.pi:
                diff_ang += 2*math.pi
                
            msg.angular.z = 6*diff_ang
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
        
        self.cmd_vel_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()