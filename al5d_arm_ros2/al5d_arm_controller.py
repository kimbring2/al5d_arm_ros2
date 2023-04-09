import rclpy
from rclpy.node import Node
import serial
import time
from std_msgs.msg import String


class AL5DSerialController(Node):
    def __init__(self):
        super().__init__('al5d_arm_controller')

        
        self.declare_parameter('serial_port', '/dev/ttyUSB0')
        self.declare_parameter('baud_rate', 115200)

        serial_port = self.get_parameter('serial_port').value
        baud_rate = self.get_parameter('baud_rate').value

        self.serial = serial.Serial(serial_port, baud_rate)
        time.sleep(2)  # Wait for the connection to be established
        
        # ros2 topic pub -r 10 /command std_msgs/msg/String "{data: '^b090s135e010w090g120w000$'}" --once
        self.subscription = self.create_subscription(
            String,
            'command',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        print("type(msg.data): ", type(msg.data))

        #command = '^b060s135e010w090g120w000$'
        command = msg.data
        command += '\n'
        self.serial.write((command).encode('utf-8'))

        #self.serial.write((msg.data).encode('utf-8'))
        time.sleep(5.0)

    def send_command(self, command):
        self.serial.write((command).encode('utf-8'))
        time.sleep(0.01)

    def close_connection(self):
        self.serial.close()


def main(args=None):
    rclpy.init(args=args)
    al5d_arm_subscriber = AL5DSerialController()

    # Example commands for the Lynxmotion AL5D arm
    # Replace these with the actual commands for your application
    #al5d_arm_controller.send_command('^b065s135e010w090g120w000$\n')
    #time.sleep(2)
    #al5d_arm_controller.send_command('^b060s135e010w090g120w000$\n')
    rclpy.spin(al5d_arm_subscriber)
    al5d_arm_subscriber.destroy_node()

    #al5d_arm_controller.close_connection()
    rclpy.shutdown()


if __name__ == '__main__':
    main()