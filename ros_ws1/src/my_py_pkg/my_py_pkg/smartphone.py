#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import String

class SmartphoneNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("Smartphone") #CHANGE NAME

        self.subscriber_ = self.create_subscribtion()
        self.get_logger().info("Smartphone has been started")
        
def main(args=None):
    rclpy.init(args=args)
    node = SmartphoneNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()