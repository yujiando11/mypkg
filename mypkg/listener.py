# SPDX-FileCopyrightText: 2023 yujiando11
# SPDX-License-Identifier: BSD-3-Clause
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

def cb(msg):
    node.get_logger().info("%3d s" % msg.data)
    if msg.data == 180:
        node.get_logger().info("180秒経ちました")
        rclpy.shutdown()
    
rclpy.init()
node = Node("listener")
sub = node.create_subscription(Int16, "countup", cb, 10)
rclpy.spin(node)


