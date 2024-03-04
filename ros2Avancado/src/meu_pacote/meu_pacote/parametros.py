import rclpy
from rclpy.node import Node, Parameter

class Parametros(Node):
    def __init__(self):
        super().__init__('Parametros')
        self.get_logger().info('Parametros iniciado')
        self.declare_parameters(
            namespace='',
            parameters=[
                ('raio_planeta', Parameter.Type.INTEGER),
                ('raio_satelite', Parameter.Type.INTEGER),
                ('nome_estrela', Parameter.Type.STRING),
                ('nome_planeta', Parameter.Type.STRING)
            ]
        )
        
        self.raio_planeta = self.get_parameter("raio_planeta").get_parameter_value().integer_value
        self.raio_satelite = self.get_parameter("raio_satelite").get_parameter_value().integer_value
        self.nome_estrela = self.get_parameter("nome_estrela").get_parameter_value().string_value
        self.nome_planeta = self.get_parameter("nome_planeta").get_parameter_value().string_value
        
        self.get_logger().info(f'raio_planeta: {self.raio_planeta}')
        self.get_logger().info(f'raio_satelite: {self.raio_satelite}')
        self.get_logger().info(f'nome_estrela: {self.nome_estrela}')
        self.get_logger().info(f'nome_planeta: {self.nome_planeta}')
        

def main(args=None):
    rclpy.init(args=args)
    parametros =  Parametros()
    rclpy.spin(parametros)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()
    