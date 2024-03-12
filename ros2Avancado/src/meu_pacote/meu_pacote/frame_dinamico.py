import rclpy
from rclpy.node import Node
import random

from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped


class FrameDinamico(Node):
    def __init__(self):
        super().__init__('FrameDinamico')
        self.get_logger().info('FrameDinamico iniciado')
        
        self._broadcaster = TransformBroadcaster(self)
        
        
        self.timer = self.create_timer(0.5, self.callback)
        self.inicio_no = self.get_clock().now()
        
    def callback(self):
        time = self.get_clock().now().seconds_nanoseconds()
        seconds = time[0] - self.inicio_no.seconds_nanoseconds()[0]
        
        distancia_x = random.randint(1, 5)
        
        t = TransformStamped()
        
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "fixed_frame" 
        t.child_frame_id = "frame_movel" 
        t.transform.translation.x = float(seconds)
        t.transform.translation.y = 0.0
        t.transform.translation.z = 0.0
        
        t.transform.rotation.x = 0.0
        t.transform.rotation.y = 0.0
        t.transform.rotation.z = 0.0
        t.transform.rotation.w = 1.0
        
        self._broadcaster.sendTransform(t)


def main(args=None):
    rclpy.init(args=args)
    frame_dinamico =  FrameDinamico()
    rclpy.spin(frame_dinamico)
    rclpy.shutdown()
    
    
    
if __name__ == '__main__':
    main()