#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from my_robot_interfaces.msg import LedStateArray
from my_robot_interfaces.srv import SetLedPanel

class LedPanelNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("led_panel_node") #CHANGE NAME
        self.led_panel_ = [0, 0, 1]
        self.led_status_publisher_ = self.create_publisher(LedStateArray, "led_status", 10)
        self.timer_ = self.create_timer(4, self.publish_led_status)
        self.server_ = self.create_service(SetLedPanel, "set_led_panel", self.callback_set_led_panel)
        self.get_logger().info("Led panel node has been started")

    def publish_led_status(self):
        msg = LedStateArray()
        msg.led_states = self.led_panel_
        self.led_status_publisher_.publish(msg)
    
    def callback_set_led_panel(self, request, response):
        led_number = request.led_number
        state = request.state

        if led_number > len(self.led_panel_) or led_number <= 0:
            response.success = False
            return response

        if state not in  [0, 1]:
            response.success = False
            return response
        
        self.led_panel_[led_number-1] = state
        response.success = True
        self.publish_led_status()
        return response

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()