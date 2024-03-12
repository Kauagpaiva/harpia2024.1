import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import random

class Publicador(Node):
    def __init__(self):
        super().__init__('publicador')
        self.get_logger().info("Publicador Iniciado")
        self._publicador = self.create_publisher(Twist, "topico1", 10)
        self.create_timer(1, self.publicar_velocidade)
        self._assinatura = self.create_subscription(String, "topico2", self.ler_modulo, 10)

    def publicar_velocidade(self):
        vel = Twist()
        vel.linear.x = random.uniform(-1.0,1.0)
        vel.linear.y = random.uniform(-1.0,1.0)
        vel.linear.z = random.uniform(-1.0,1.0)

        vel.angular.x = random.uniform(-1.0,1.0)
        vel.angular.y = random.uniform(-1.0,1.0)
        vel.angular.z = random.uniform(-1.0,1.0)

        self._publicador.publish(vel)

    def ler_modulo(self, msg):
        self.get_logger().info(msg)

def main(args=None):
    rclpy.init(args=args)
    publicador = Publicador()
    rclpy.spin(publicador)
    rclpy.shutdown()

if __name__ == '__main__':
    main()