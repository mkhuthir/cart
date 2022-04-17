cmake_minimum_required(VERSION 3.5.0)
project(gz_ros2_control)

# Default to C11
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 11)
endif()
# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(NOT WIN32)
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(control_msgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclcpp_action REQUIRED)
find_package(std_msgs REQUIRED)

install(DIRECTORY
  launch
  config
  urdf
  DESTINATION share/${PROJECT_NAME}/
)

add_executable(position examples/position.cpp)
ament_target_dependencies(position
  rclcpp
  rclcpp_action
  control_msgs
)

add_executable(velocity examples/velocity.cpp)
ament_target_dependencies(velocity
  rclcpp
  std_msgs
)

add_executable(effort examples/effort.cpp)
ament_target_dependencies(effort
  rclcpp
  std_msgs
)

add_executable(gripper examples/gripper)
ament_target_dependencies(gripper
  rclcpp
  std_msgs
)

if(BUILD_TESTING)
  find_package(ament_cmake_gtest REQUIRED)
  find_package(ament_lint_auto REQUIRED)

  ament_lint_auto_find_test_dependencies()
endif()

## Install
install(TARGETS position velocity effort gripper
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
