#!/usr/bin/env python3
import rclpy
import math
from rclpy.node import Node

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim_project_interfaces.msg import Turtle
from turtlesim_project_interfaces.msg import TurtleArray

class TurtleControllerNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("turtle_controller") #CHANGE NAME

        self.turtle_to_catch = None
        
        self.pose_ = None

        self.cmd_vel_publisher_ = self.create_publisher(Twist, "turtle1/cmd_vel", 10)
        self.subscriber_ = self.create_subscription(Pose, "turtle1/pose", self.callback_Turtle_Position, 10)

        self.alive_turtles_subscriber_ = self.create_subscription(TurtleArray, "alive_turtles", self.callback_alive_turtles, 10)
        
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.get_logger().info("Turtle controller node has been started")

    def callback_Turtle_Position(self, msg):
        self.pose_ = msg

    def callback_alive_turtles(self, msg):
        if len(msg.turtles) > 0:
            self.turtles_to_catch = msg.turtles[0]

    def control_loop(self):
        if self.pose_ == None or self.turtle_to_catch == None:
            return
        
        distance_x = self.turtle_to_catch.x - self.pose_.x
        distance_y = self.turtle_to_catch.y - self.pose_.y
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