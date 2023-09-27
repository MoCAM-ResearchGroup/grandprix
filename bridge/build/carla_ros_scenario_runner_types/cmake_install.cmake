# Install script for directory: /home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types/srv" TYPE FILE FILES "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types/srv/ExecuteScenario.srv")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types/msg" TYPE FILE FILES
    "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types/msg/CarlaScenario.msg"
    "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types/msg/CarlaScenarioList.msg"
    "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types/msg/CarlaScenarioRunnerStatus.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types/cmake" TYPE FILE FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner_types/catkin_generated/installspace/carla_ros_scenario_runner_types-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/devel/include/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/devel/share/roseus/ros/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/devel/share/common-lisp/ros/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/devel/share/gennodejs/ros/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/iotsc/grandprix/bridge/devel/lib/python3/dist-packages/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/iotsc/grandprix/bridge/devel/lib/python3/dist-packages/carla_ros_scenario_runner_types")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner_types/catkin_generated/installspace/carla_ros_scenario_runner_types.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types/cmake" TYPE FILE FILES "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner_types/catkin_generated/installspace/carla_ros_scenario_runner_types-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types/cmake" TYPE FILE FILES
    "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner_types/catkin_generated/installspace/carla_ros_scenario_runner_typesConfig.cmake"
    "/home/iotsc/grandprix/bridge/build/carla_ros_scenario_runner_types/catkin_generated/installspace/carla_ros_scenario_runner_typesConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/carla_ros_scenario_runner_types" TYPE FILE FILES "/home/iotsc/grandprix/bridge/src/carla_ros_scenario_runner_types/package.xml")
endif()

