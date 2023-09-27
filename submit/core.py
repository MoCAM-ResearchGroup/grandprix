import numpy as np
import rospy
from math import atan2, sin, cos
from visualization_msgs.msg import MarkerArray, Marker
from carla_msgs.msg import CarlaEgoVehicleControl
import sys
from nav_msgs.msg import Odometry, Path
from derived_object_msgs.msg import ObjectArray
import imp
from geometry_msgs.msg import PoseStamped

class core:
    def __init__(self, planner_file_name='motion_planner.py') -> None:
        
        rospy.init_node('run', anonymous=True)

        # subscribe
        rospy.Subscriber("/carla/ego_vehicle/odometry", Odometry, self.odometry_callback)    
        rospy.Subscriber("/carla/ego_vehicle/objects", ObjectArray, self.obstacle_callback)    


        # publish
        self.pub_marker_car = rospy.Publisher('/carla/ego_vehicle/car_marker', MarkerArray, queue_size=10)
        self.pub_vel = rospy.Publisher('/carla/ego_vehicle/vehicle_control_cmd', CarlaEgoVehicleControl, queue_size=10) 
        # self.pub_current_path = rospy.Publisher('/carla/ego_vehicle/current_path', Path, queue_size=10)
        self.pub_marker_obs = rospy.Publisher('/carla/ego_vehicle/obs_marker', MarkerArray, queue_size=10)
        self.pub_path = rospy.Publisher('reference_path', Path, queue_size=10)
        # self.pub_opt_path = rospy.Publisher('opt_path', Path, queue_size=10)

        # information
        txt_path = sys.path[0] + '/ref_path.txt'
        point_array = np.loadtxt(txt_path)
        self.ref_path_list = [ np.c_[point] for point in point_array] # reference path for vehicle

        self.robot_state = self.ref_path_list[0].copy()  # robot state: x, y, theta (yaw)
        self.shape = [4.69, 1.85, 2.87, 1.75]  # length, width, wheelbase, width_wheelbase; All the objects are with this shape
        self.obstacle_list = []  # list of obstacles states, each obstacle is a (3, 1) matrix (x, y, theta); The shape of the obstacle is same with the robot (self.shape)

        # Plot Message in rviz
        self.marker_array_car = MarkerArray()  # plot car marker
        self.marker_array_obs = MarkerArray()  # plot obstacle marker
        self.marker_array_path = MarkerArray() # plot path marker 

        self.path_line = self.generate_path(self.ref_path_list)

        self.output_control = CarlaEgoVehicleControl()

        abs_path = sys.path[0] + '/answers/' + planner_file_name
        planner_class = imp.load_source('planner_class', abs_path)
        self.mp = planner_class.motion_planner(self.shape, self.ref_path_list)


    def publisher(self):

        rate = rospy.Rate(50) # 10hz

        while rospy.is_shutdown() is False:

            vel  = self.mp.calculate_velocity(self.robot_state, self.obstacle_list)

            self.output_control.throttle = vel[0, 0]
            self.output_control.steer = vel[1, 0]

            if vel[0, 0] <= 0.05:
                self.output_control.brake = 1.0
            else:
                self.output_control.brake = 0.0

            # publish topic
            self.pub_marker_car.publish(self.marker_array_car)
            self.pub_marker_obs.publish(self.marker_array_obs)
            self.pub_path.publish(self.path_line)
            self.pub_vel.publish(self.output_control)

            # self.pub_vel.publish(self.output_control)
            # temp_opt_path_list = list(opt_path.T)
            # opt_path_list = [ np.c_[point]  for point in temp_opt_path_list]

            # opt_path_line = self.generate_path(opt_path_list)
            # self.pub_opt_path.publish(opt_path_line)

            rospy.loginfo_once("Publish car marker sueccessfully")
            rospy.loginfo_throttle(2, "Publish Velocity {} sueccessfully".format(vel))

            rate.sleep()


    def odometry_callback(self, data):

        self.marker_array_car = MarkerArray()

        x = data.pose.pose.position.x
        y = data.pose.pose.position.y
        z = data.pose.pose.position.z

        quat = data.pose.pose.orientation

        raw = core.quat_to_yaw(quat)

        offset = self.shape[2] / 2
            
        self.robot_state[0] = x - offset * cos(raw)
        self.robot_state[1] = y - offset * sin(raw)
        self.robot_state[2] = raw

        marker = Marker()

        marker.header.frame_id = 'map'
        marker.header.seq = 0
        marker.header.stamp = rospy.get_rostime()

        marker.id = 100
        marker.type = 1

        marker.scale.x = 4.7
        marker.scale.y = 1.9
        marker.scale.z = 1.6
        marker.color.a = 1.0
        marker.color.r = 255/255
        marker.color.g = 0/255
        marker.color.b = 255/255

        marker.pose.position.x = x
        marker.pose.position.y = y
        marker.pose.position.z = z
        marker.pose.orientation = quat

        self.marker_array_car.markers.append(marker)


    def obstacle_callback(self, data):

        self.marker_array_obs = MarkerArray()

        self.obstacle_list = []

        for i, object_data in enumerate(data.objects):

            pose_x = object_data.pose.position.x
            pose_y = object_data.pose.position.y
            pose_z = object_data.pose.position.z

            quat = object_data.pose.orientation
            yaw = core.quat_to_yaw(quat) 

            self.obstacle_list.append(np.array([pose_x, pose_y, yaw]).reshape(3, 1))

            marker = Marker()
            marker.header.frame_id = 'map'
            marker.header.seq = 0
            marker.header.stamp = rospy.get_rostime()

            marker.scale.x = 4.7
            marker.scale.y = 1.8
            marker.scale.z = 1.4
            marker.color.a = 1.0
            marker.color.r = 30/255
            marker.color.g = 144/255
            marker.color.b = 255/255

            # marker.id = self.marker_id + 1
            # self.marker_id = self.marker_id + 1
            marker.id = i + 1
            marker.type = 1
            marker.pose.position.x = pose_x
            marker.pose.position.y = pose_y
            marker.pose.position.z = pose_z + marker.scale.z/2
            marker.pose.orientation = quat

            self.marker_array_obs.markers.append(marker)

    

    @staticmethod
    def generate_path(ref_path_list):
        path = Path()

        path.header.seq = 0
        path.header.stamp = rospy.get_rostime()
        path.header.frame_id = 'map'

        for i in range(len(ref_path_list)):
            ps = PoseStamped()
            ps.pose.position.x = ref_path_list[i][0, 0]
            ps.pose.position.y = ref_path_list[i][1, 0]
            ps.pose.position.z = 0

            path.poses.append(ps)

        return path


    @staticmethod
    def quat_to_yaw(quater):
        
        w = quater.w
        x = quater.x
        y = quater.y
        z = quater.z

        raw = atan2(2* ( w*z + x *y), 1 - 2 * (pow(z, 2) + pow(y, 2)))

        return raw



    


   
  
