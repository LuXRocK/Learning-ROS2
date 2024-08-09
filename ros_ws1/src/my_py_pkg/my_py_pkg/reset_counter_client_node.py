import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts
from example_interfaces.srv import SetBool

class ResetCounterClientNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("ResetCounterClientNode") #CHANGE NAME
        self.call_reset_counter_server(True) #CHANGE FUNCTIONALITY

    def call_reset_counter_server(self, r):
        client = self.create_client(SetBool, "reset_counter") #CHANGE NAME
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")

        request = SetBool.Request()
        request.data = r

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, r=r))

    def callback_call_add_two_ints(self, future, r):
        try:
            response = future.result()
            self.get_logger().info("Request data is: " + str(r) + " which results in response: " + str(response.success))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = ResetCounterClientNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()