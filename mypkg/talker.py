import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.season == "四季":
        response.spring = "少しずつ暖かくなり過ごしやすいです。桜の花が咲きます。"
        response.summer = "雨がたくさん降る時期があり、その後暑さが増します。夏祭りや花火があります。"
        response.fall = "暑さがやわらぎます。紅葉がよく見られます。"
        response.winter = "気温が下がり、寒さが増します。雪景色が見られます。"
    else:
        response.other = "分かりません"
    
    return response

rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
