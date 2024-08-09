import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class ClientNode(Node): #CHANGE NAME
    def __init__(self):
        super().__init__("ClientNode") #CHANGE NAME
        self.call_add_two_ints_server(1, 1) #CHANGE FUNCTIONALITY

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(AddTwoInts, "ClientNode") #CHANGE NAME
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for Server Add Two Ints...")

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(self.callback_call_add_two_ints, a=a, b=b))

    def callback_call_add_two_ints(self, future, a, b):
        try:
            response = future.result()
            self.get_logger().info(str(a) + " + " + str(b) + " = " + str(response.sum))
        except Exception as e:
            self.get_logger().error("Service call failed %r" % (e,))

def main(args=None):
    rclpy.init(args=args)
    node = ClientNode() #CHANGE NAME
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()