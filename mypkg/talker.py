import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "四季":
        response.season = "\n・春:少しずつ暖かくなり過ごしやすいです。桜の花が咲きます。\n・夏:雨がたくさん降る時期があり、その後暑さが増します。夏祭りや花火があります。\n・秋:暑さがやわらぎます。紅葉がよく見られます。\n・冬:気温が下がり、寒さが増します。雪景色が見られます。\n"
    else:
        response.season = "分かりません"
    
    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
