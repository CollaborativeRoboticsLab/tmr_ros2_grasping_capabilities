cmake_minimum_required(VERSION 3.8)
project(omron_grasping_capabilities)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch plans providers semantic_interfaces
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
