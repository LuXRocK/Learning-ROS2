#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64

class NumberCounterNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("number_counter") #CHANGE NAME

        self.counter_ = 0

        self.publisher_ = self.create_publisher(Int64, "number_count", 10)
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number_data, 10)
        self.get_logger().info("Number counter node has been started")

    def callback_number_data(self, msg):
        self.counter_ += msg.data
        new_msg = Int64() 
        new_msg.data = self.counter_
        self.publisher_.publish(new_msg)
        # self.get_logger().info(str(msg.data))
    
    # def publish_data(self):
    #     msg = Int64()
    #     msg.data = self.new_number_
    #     self.publisher_.publish(msg)
        
    
def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()