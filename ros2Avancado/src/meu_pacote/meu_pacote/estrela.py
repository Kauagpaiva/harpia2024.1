import rclpy
from rclpy.node import Node, Parameter


from tf2_ros import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped


class Estrela(Node):
    def __init__(self):
        super().__init__('Estrela')
        self.get_logger().info('Estrela iniciada')

        self._broadcaster = StaticTransformBroadcaster(self)
        self.nome_estrela = self.get_parameter("nome_estrela").get_parameter_value().string_value #Não to conseguindo ler os parametros
        
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "universo" 
        t.child_frame_id = self.nome_estrela 
        t.transform.translation.x = 0.0
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self._broadcaster.sendTransform(t)




def main(args=None):
    rclpy.init(args=args)
    estrela =  Estrela()
    rclpy.spin(estrela)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()