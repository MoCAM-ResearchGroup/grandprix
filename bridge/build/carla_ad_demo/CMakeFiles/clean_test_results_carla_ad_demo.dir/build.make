# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/iotsc/grandprix/bridge/src

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/iotsc/grandprix/bridge/build

# Utility rule file for clean_test_results_carla_ad_demo.

# Include the progress variables for this target.
include carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/progress.make

carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo:
	cd /home/iotsc/grandprix/bridge/build/carla_ad_demo && /usr/bin/python3 /opt/ros/noetic/share/catkin/cmake/test/remove_test_results.py /home/iotsc/grandprix/bridge/build/test_results/carla_ad_demo

clean_test_results_carla_ad_demo: carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo
clean_test_results_carla_ad_demo: carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/build.make

.PHONY : clean_test_results_carla_ad_demo

# Rule to build all files generated by this target.
carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/build: clean_test_results_carla_ad_demo

.PHONY : carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/build

carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/clean:
	cd /home/iotsc/grandprix/bridge/build/carla_ad_demo && $(CMAKE_COMMAND) -P CMakeFiles/clean_test_results_carla_ad_demo.dir/cmake_clean.cmake
.PHONY : carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/clean

carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/depend:
	cd /home/iotsc/grandprix/bridge/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/iotsc/grandprix/bridge/src /home/iotsc/grandprix/bridge/src/carla_ad_demo /home/iotsc/grandprix/bridge/build /home/iotsc/grandprix/bridge/build/carla_ad_demo /home/iotsc/grandprix/bridge/build/carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : carla_ad_demo/CMakeFiles/clean_test_results_carla_ad_demo.dir/depend

