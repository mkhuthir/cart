#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray    


class cartPub(Node):
    def __init__(self):
        super().__init__('cartVelocityNode')

def main(args=None):
    rclpy.init(args=args)

    node = cartPub()
    
    msg = Float64MultiArray()
    msg.data = [1.0]
    
    node.get_logger().info("Hello from node")

    rclpy.spin(node)
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
