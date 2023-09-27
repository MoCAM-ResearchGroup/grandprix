import numpy as np
from math import atan2, sin, cos, sqrt, pi, inf, tan
import copy
class motion_planner:
    def __init__(self, shape, ref_path_list):
        r"""
        @param shape: list of the vehicle shape [length, width, wheelbase, width_wheelbase] 
        @param ref_path_list: the reference path that the vehicle should follow
        """
        self.ref_path_list = ref_path_list
        self.shape = shape

        "*** YOUR CODE STARTS HERE ***"
        self.Lfc = 3.5  # [m]look forward distance
        self.WB = self.shape[2] # [m]wheelbase

        self.cur_index = 0
        self.ref_speed = 5.0 #[m] reference speed
        self.min_speed = 1.5

        self.max_steer_angle = 70.0

        "*** YOUR CODE END HERE ***"

    def calculate_velocity(self, robot_state, obstacle_list):
        r"""
        The function of calculating the velocity from the robot and environment information
        
        Some parameters that you may use:
        @param robot_state: 3 *1 matrix,  [x, y, theta(heading direction)] of the robot. 
        
        @param obstacle_list: list of obstacles
        

        Return:
        @param velocity: 2*1 matrix, linear speed, steering. 
                         Notation: The range of linear speed and steering should be normalized in [0, 1] and [-1, 1]
        """

        "*** YOUR CODE STARTS HERE ***"

        min_dis, min_ind = self.closest_point(robot_state,self.ref_path_list,self.cur_index)
        self.cur_index = min_ind

        local_wps = self.find_target(state = robot_state,ref_path = self.ref_path_list,start_ind = min_ind)
        target_wp = local_wps[-1]

        steer, alpha = self.purepursuit(robot_state, target_wp)

        # norm to [-1,1]
        steer = steer*180.0/(pi*self.max_steer_angle)
        steer = 1.0 if abs(steer)>1.0 else steer
        steer = -abs(steer) if alpha > 0 else abs(steer)
        
        # change velocity according to the steer angle 
        speed = -(self.ref_speed-self.min_speed)*(abs(steer)-1.0)**5 + self.min_speed

        if self.cur_index == len(self.ref_path_list) - 1:
            return np.array([[0.0],[0.0]])

        return np.array([[speed/10.0],[steer]])

    def purepursuit(self,robot_state, target_wp):
        state = robot_state
        ld = motion_planner.distance(state[0:2], target_wp[0:2])

        cur_yaw = state[2,0]
        alpha = motion_planner.angle(np.array([np.cos(cur_yaw),np.sin(cur_yaw),0.0]),np.array([target_wp[0,0]-state[0,0],target_wp[1,0]-state[1,0],0.0]))

        steer = atan2(2.0*self.WB*sin(abs(alpha)),ld) 
        return steer, alpha
    
    def decision(self,vel,robot_state,obstacle_list):
        pass

    def closest_point(self, state, ref_path, start_ind, threshold=0.1, ind_range=15):
        
        min_dis = inf
        min_ind = start_ind # if start_ind-2 < 0 else start_ind - 2
    
        for i, waypoint in enumerate(ref_path[start_ind:start_ind+ind_range]):
            dis = motion_planner.distance(state[0:2], waypoint[0:2])
            if dis < min_dis:
                min_dis = dis
                min_ind = start_ind + i
                if dis < threshold: break
                    
        return min_dis, min_ind
    
    def find_target(self, state, ref_path, start_ind,**kwargs):
        lastwp = state[0:2]
        acc_len = 0.0
        local_wps=[] # local waypoint list: from current waypoint to the target waypiont
        for i,waypoint in enumerate(ref_path[start_ind:]):
            dis = motion_planner.distance(lastwp, waypoint[0:2])
            acc_len += dis
            if acc_len > self.Lfc:
                local_wps.append(waypoint[0:2])
                break
            lastwp = waypoint[0:2]
            local_wps.append(lastwp)
        return local_wps
    

    def curvature(x,y):
        """
        input  : the coordinate of the three point
        output : the curvature and norm direction
        refer to https://github.com/Pjer-zhang/PJCurvature for detail
        """
        t_a = np.linalg.norm([x[1]-x[0],y[1]-y[0]])
        t_b = np.linalg.norm([x[2]-x[1],y[2]-y[1]])
        
        M = np.array([
            [1, -t_a, t_a**2],
            [1, 0,    0     ],
            [1,  t_b, t_b**2]
        ])

        a = np.matmul(np.linalg.inv(M),x)
        b = np.matmul(np.linalg.inv(M),y)

        kappa = 2*(a[2]*b[1]-b[2]*a[1])/(a[1]**2.+b[1]**2.)**(1.5)
        return kappa, [b[1],-a[1]]/np.sqrt(a[1]**2.+b[1]**2.)

    @staticmethod
    def distance(point1, point2):
        return sqrt( (point1[0, 0] - point2[0, 0])**2 + (point1[1, 0] - point2[1, 0])**2 )

    @staticmethod
    def wraptopi(radian):
        while radian > pi:
            radian = radian - 2 * pi
        while radian < -pi:
            radian = radian + 2 * pi

        return radian 
    
    @staticmethod
    def angle(v1, v2):
        # from v1 to v2
 
        norm = np.linalg.norm(v1) * np.linalg.norm(v2)

        rho_z = np.cross(v1, v2)[-1]

        theta = np.arccos(np.dot(v1, v2) / norm)
        if rho_z < 0:
            return - theta
        else:
            return theta
    "*** YOUR CODE END HERE ***"