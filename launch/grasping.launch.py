from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    motion_execution_launch = PathJoinSubstitution([
        FindPackageShare('grasping_control'), 'launch', 'motion_execution.launch.py'])
    motion_config = PathJoinSubstitution([
        FindPackageShare('omron_grasping_capabilities'), 'config', 'motion_config.yaml'])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(motion_execution_launch),
            launch_arguments={
                'motion_config_file': motion_config,
                'workspace_file': 'config/crlab_table.yaml',
                'default_scene_name': 'crlab_table',
                'default_scene_package': 'grasping_omron_moma',
                'launch_feasiblity_service': 'true',
            }.items(),
        ),
    ])