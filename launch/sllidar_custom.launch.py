from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='sllidar_ros2',
            executable='sllidar_node',
            name='sllidar_node',
            output='screen',
            parameters=[{
                'serial_port': '/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',  # RPLidar stable device path
                'serial_baudrate': 115200,   # RPLidar A1 default baudrate
                'frame_id': 'laser_frame',
                'inverted': False,
                'angle_compensate': True
            }]
        )
    ])

