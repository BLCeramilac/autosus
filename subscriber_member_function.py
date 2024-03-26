
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.publisher_ = self.create_publisher(Int32, 'kvadrat_broja', 10)
        self.subscription = self.create_subscription(
            Int32,
            'broj',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        squared = Int32()
        squared.data = msg.data ** 2
        self.publisher_.publish(squared)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
