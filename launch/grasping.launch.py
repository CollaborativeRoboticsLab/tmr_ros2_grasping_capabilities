from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    robot_ip = LaunchConfiguration('robot_ip')
    use_simulation = LaunchConfiguration('use_simulation')
    tmr_moveit_launch = PathJoinSubstitution([
        FindPackageShare('tm12x_moveit_config'), 'launch', 'tm12x_run_move_group.launch.py'])
    motion_execution_launch = PathJoinSubstitution([
        FindPackageShare('grasping_control'), 'launch', 'motion_execution.launch.py'])
    motion_config = PathJoinSubstitution([
        FindPackageShare('tmr_ros2_grasping_capabilities'), 'config', 'motion_config.yaml'])

    return LaunchDescription([
        DeclareLaunchArgument(
            'robot_ip',
            default_value='192.168.1.2',
            description='TMR robot IP address',
        ),
        DeclareLaunchArgument(
            'use_simulation',
            default_value='false',
            description='Start the TMR driver in simulation mode',
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(tmr_moveit_launch),
            launch_arguments={
                'robot_ip': robot_ip,
                'use_simulation': use_simulation,
            }.items(),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(motion_execution_launch),
            launch_arguments={
                'motion_config_file': motion_config,
                'startup_activate_default_scene': 'false',
                'launch_feasiblity_service': 'true',
            }.items(),
        ),
    ])