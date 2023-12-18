import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, "query")
    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('待機中')

    req = Query.Request()
    req.season = "四季"
    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else:
                node.get_logger().info("\n春:{}\n夏:{}\n秋:{}\n冬:{}\n".format(response.spring, response.summer, response.fall, response.winter))
            
            break
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
