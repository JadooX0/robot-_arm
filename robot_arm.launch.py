from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Launch gz sim (use appropriate package/launch)
    gz = ExecuteProcess(cmd=['gz', 'server', '--verbose'], shell=False)

    # spawn_entity node - spawn robot into Gazebo from URDF
    spawn = Node(package='ros_gz_sim', executable='create', arguments=['-name', '3dof_arm', '-file', '/path/to/3dof_arm.urdf'])

    # controller manager (ros2_control_node)
    controller_manager = Node(
        package='controller_manager',
        executable='ros2_control_node',
        parameters=['/path/to/your/robot.ros2_control.yaml', '/path/to/controllers.yaml'],
        output='screen'
    )

    return LaunchDescription([gz, spawn, controller_manager])
