# CARLA-ROS-RDA Bridge

Download the CARLA-MAP from [here]()

# Prerequisite

- Platform:
  - Python >= 3.8
  - Ubnutu 20.04
  - ROS Noetic


```
sudo apt-get install ros-noetic-carla-msgs ros-noetic-ackermann-msgs ros-noetic-derived-object-msgs
```

```
pip install numpy cvxpy transforms3d pygame
```

# Environment Variables

```
export CARLA_ROOT=<path-to-carla>
export PYTHONPATH=$PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-<carla_version_and_arch>.egg:$CARLA_ROOT/PythonAPI/carla
```
For example:

```
export CARLA_ROOT=~/grandprix/map
export PYTHONPATH=$PYTHONPATH:$CARLA_ROOT/PythonAPI/carla/dist/carla-0.9.13-py3.8-linux-x86_64.egg:$CARLA_ROOT/PythonAPI/carla
```

# Start CARLA server

```
cd $CARLA_ROOT
./CarlaUE4.sh
```

# Build the ros-bridge

```
cd bridge
catkin_make
source devel/setup.bash
```

Note: you may need to run 
```
cd src/carla_ros_bridge/src/carla_ros_bridge
chmod +x bridge.py 
```

# Spawn agents and Start CARLA-ROS-Bridge

```
roslaunch carla_ros_bridge test.launch
``` 


# Complete the file motion_planner.py in submit

- core.py: The core file to implement the MPC controller
- ref_path.txt: The reference path file
- run.py: The file to run the ROS node
- answers/example_motion_planner.py: The example answer file that you can refer to 
- **answers/motion_planner.py**: The file should to be completed

# Run example answers

First, put the python file in the folder submit/answers. Then, run the following command:

```
python submit/run.py -f YOUR_FILE_NAME
```

For example, to run the MPC path tracking, the command should be:

```
python submit/run.py -f 'example_motion_planner_mpc.py'
```


For example, to run the pure pursuit path tracking, the command should be:

```
python submit/run.py -f 'example_motion_planner_purepursuit.py'
```



