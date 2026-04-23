#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounterNode(Node): 
    def __init__(self):
        self.counter = 0
        super().__init__("number_counter") 
        self.subscriber_ = self.create_subscription(
            Int64, "number",self.callback_number_publisher, 10)
        self.get_logger().info("Number Counter has been started!")
        self.publisher = self.create_publisher(Int64, "number_count", 10)

    
    def callback_number_publisher(self, msg: Int64):
        self.get_logger().info(f"data: {msg.data}")
        self.counter += int(msg.data)
        counter_otimizado = Int64()
        counter_otimizado.data = self.counter
        self.publisher.publish(counter_otimizado)
        self.get_logger().info(f"Count value: {self.counter}")
        

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
