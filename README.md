# Grand Prix Metaverse Autonomous Driving Challenge

<img src="./assets/banner.png" width=600px>

<a href="https://youtu.be/48-6jFwECa4"><img src="https://i.ytimg.com/vi/48-6jFwECa4/maxresdefault.jpg" alt="" width="600px"></a>

Contest website: https://contests.cis.um.edu.mo/meta_racing_2023

# Prerequisite

- Platform:
  - Python >= 3.8
  - Ubnutu 20.04
  - ROS Noetic: http://wiki.ros.org/noetic/Installation/Ubuntu
  - Download the CARLA-MAP: 
[Google Drive  ](https://drive.google.com/file/d/1mrN5Huq_dLB-yfFZw-MomFVwu-8GEwfn/view?usp=sharing) 
/
[  Baidu Pan](https://pan.baidu.com/s/1Jd10r2cOC9FVueip3ZMT_Q) (提取码: absd)


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

# Testing with NPC agent


In this challenge, you have to deal with situations where other vehicles appear on the track at the same time. The ego-vehicle should avoid or change lanes independently to complete the race. Therefore, we have a script to generate a NPC vehicle in a random spawn point.

```
python testing/vehicle_random_generate.py
```

   change the control mode of the NPC vehicle

```
# ego control mode, "set_transform" OR "ackermann_control" OR "control" OR "autopilot" "stop"

CONTROL_MODE = "autopilot"
```

