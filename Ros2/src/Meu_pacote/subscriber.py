import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist


class Assinante(Node):
    def __init__(self):
        super().__init__('Assinante')
        self.get_logger().info('Escutando topico')
        self._publicador = self.create_publisher(String, "topico2", 10)
        self._assinatura = self.create_subscription(Twist, "topico1", self.criar_modulo, 10)
       
    
    def criar_modulo(self, vel):
        modulo_linear = (vel.linear.x**2 + vel.linear.y**2 + vel.linear.z**2)**(1/2)
        modulo_angular = (vel.angular.x**2 + vel.angular.y**2 + vel.angular.z**2)**(1/2)

        msg = String()
        msg.data = "Modulo Linear: {}, Modulo Angular: {}".format(modulo_linear, modulo_angular)

        mensagem = msg.data
        self._publicador.publish(mensagem)


def main(args=None):
    rclpy.init(args=args)
    assinante =  Assinante()
    rclpy.spin(assinante)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()