from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    
    config = os.path.join(
        get_package_share_directory('meu_pacote'),
        'config',
        'param.yaml'
        )

    
    return LaunchDescription([
        
        Node( #Não funciona desse jeito, que nem foi mostrado na aula, o de baixo funciona.
            package="meu_pacote",
            executable="parametros",
            name="parametros",
            parameters=[config]
        ),
        # Node(
        #     package="meu_pacote",
        #     executable="parametros",
        #     name="parametros",
        #     parameters=[
        #         {"raio_planeta":2},
        #         {'raio_satelite': 1},
        #         {'nome_estrela': "Sol"},
        #         {"nome_planeta": "Terra"}
        #     ]
        # ),
        Node(
            package="meu_pacote",
            executable="estrela",
            name="estrela",
        ), 
        Node(
            package="meu_pacote",
            executable="planeta",
            name="planeta",
        ),
        Node(
            package="meu_pacote",
            executable="satelite",
            name="satelite",
        ),
    ])