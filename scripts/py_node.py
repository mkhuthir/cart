#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float64MultiArray    



class cartPublisher(Node):

    def __init__(self):
        super().__init__('my_node')
        self.publisher_ = self.create_publisher(Float64MultiArray, '/effort_controllers/commands', 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Float64MultiArray
        msg.data[0] = 100
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing')
        self.i += 10


def main(args=None):
    rclpy.init(args=args)

    my_node = cartPublisher()

    rclpy.spin(my_node)
    
    my_node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
