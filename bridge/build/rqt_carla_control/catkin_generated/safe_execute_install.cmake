execute_process(COMMAND "/home/iotsc/grandprix/bridge/build/rqt_carla_control/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/iotsc/grandprix/bridge/build/rqt_carla_control/catkin_generated/python_distutils_install.sh) returned error code ")
endif()