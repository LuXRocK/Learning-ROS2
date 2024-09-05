#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from turtlesim.msg import Pose

class TurtleControllerNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("turtle_controller") #CHANGE NAME

        self.subscriber_ = self.create_subscription(Pose, "/turtle1/pose", self.callbackTurtlePosition, 10)
        self.get_logger().info("Turtle controller node has been started")

    def callbackTurtlePosition(self, msg):
        x_ = msg.x
        y_ = msg.y
        theta_ = msg.theta
        l_vel_ = msg.linear_velocity
        a_vel_ = msg.angular_velocity
        self.get_logger().info("Turtle is at position: x = " + str(x_) + " , y = " + str(y_))
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()