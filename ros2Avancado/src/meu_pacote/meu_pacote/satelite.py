import rclpy
from rclpy.node import Node, Parameter
import math
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped


class Satelite(Node):
    def __init__(self):
        super().__init__('Satelite')
        self.get_logger().info('Satelite iniciado')
        
        self._broadcaster = TransformBroadcaster(self)
        #Não to conseguindo ler os parametros, essa parte da erro
        self.raio_satelite = self.get_parameter("raio_satelite").get_parameter_value().integer_value
        self.nome_planeta = self.get_parameter("nome_planeta").get_parameter_value().string_value
        
        self.timer = self.create_timer(0.5, self.callback)
        
    def callback(self):
        angulo = self.get_clock().now().to_msg().sec
        x = self.raio_satelite * math.cos(angulo)
        y = self.raio_satelite * math.sin(angulo)
        t = TransformStamped()
        
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = self.nome_planeta
        t.child_frame_id = "lua" 

        t.transform.translation.x = x
        t.transform.translation.y = y
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self._broadcaster.sendTransform(t)


def main(args=None):
    rclpy.init(args=args)
    satelite =  Satelite()
    rclpy.spin(satelite)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()