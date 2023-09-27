execute_process(COMMAND "/home/iotsc/grandprix/bridge/build/ros_compatibility/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/iotsc/grandprix/bridge/build/ros_compatibility/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
