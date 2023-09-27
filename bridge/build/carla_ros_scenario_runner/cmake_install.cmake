# Install script for directory: /home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/iotsc/grandprix/bridge/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  include("/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/safe_execute_install.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/carla_ros_scenario_runner.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner/cmake" TYPE FILE FILES
    "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/carla_ros_scenario_runnerConfig.cmake"
    "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/carla_ros_scenario_runnerConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner" TYPE FILE FILES "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner/package.xml")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/carla_ros_scenario_runner" TYPE PROGRAM FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/carla_ros_scenario_runner_node.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/carla_ros_scenario_runner" TYPE PROGRAM FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/application_runner.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/carla_ros_scenario_runner" TYPE PROGRAM FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/scenario_runner_runner.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/carla_ros_scenario_runner" TYPE PROGRAM FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner/catkin_generated/installspace/ros_vehicle_control.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner/launch" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner/launch/")
endif()

