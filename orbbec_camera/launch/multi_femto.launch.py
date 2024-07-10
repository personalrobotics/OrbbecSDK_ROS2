from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, GroupAction, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():
    # Include launch files
    package_dir = get_package_share_directory('orbbec_camera')
    launch_file_dir = os.path.join(package_dir, 'launch')
    launch1_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'femto_bolt.launch.py')
        ),
        launch_arguments={
            'camera_name': 'front_camera',
            'usb_port': '2-2',
            # 'usb_port': '2-9.2.1',
            # 'serial_number': 'CL8K14100WH',
            'device_num': '2',
            'sync_mode': 'standalone',
            'enable_colored_point_cloud': 'true'
        }.items()
    )

    launch2_include = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(launch_file_dir, 'femto_bolt.launch.py')
        ),
        launch_arguments={
            'camera_name': 'top_camera',
            'usb_port': '2-3',
            # 'usb_port': '2-9.1.4',
            # 'serial_number': 'CL8K14101DW',
            'device_num': '2',
            'sync_mode': 'standalone',
            'enable_colored_point_cloud': 'true'
        }.items()
    )

    # If you need more cameras, just add more launch_include here, and change the usb_port and device_num

    # Launch description
    ld = LaunchDescription([
        GroupAction([launch1_include]),
        GroupAction([launch2_include]),
    ])

    return ld
