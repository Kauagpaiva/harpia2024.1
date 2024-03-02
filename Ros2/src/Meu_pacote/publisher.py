import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class Publicador(Node):
    def __init__(self):
        super().__init__('publicador')
        self.get_logger().info("Publicador Iniciado")
        self._publicador = self.create_publisher(Twist, "topico1", 10)
        self.create_timer(1, self.callback)
        self._assinatura = self.create_subscription(String, "topico2", self.callback2, 10)

    def callback(self):
        vel = Twist()
        vel.linear.x = 0.0
        vel.linear.y = 0.0
        vel.linear.z = 0.0

        vel.angular.x = 0.0
        vel.angular.y = 0.0
        vel.angular.z = 0.0

        self._publicador.publish(vel)

    def callback2(self, msg):
        self.get_logger().info(msg)

def main(args=None):
    rclpy.init(args=args)
    publicador = Publicador()
    rclpy.spin(publicador)
    rclpy.shutdown()

if __name__ == '__main__':
    main()