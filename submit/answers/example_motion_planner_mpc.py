import numpy as np
import cvxpy as cp
from math import atan2, sin, cos, sqrt, pi, inf, tan


class motion_planner:
    def __init__(self, shape, ref_path_list):

        r"""
        @param shape: list of the vehicle shape [length, width, wheelbase, width_wheelbase] 
        @param ref_path_list: the reference path that the vehicle should follow
        """

        self.ref_path_list = ref_path_list
        self.shape = shape
        

        "*** YOUR CODE STARTS HERE ***"
        # You can define your own instance attributes here

        self.T = 20 # receding horizon length
        self.cur_vel_array = np.zeros((2, self.T))
        self.sample_time = 0.3
        self.cur_index = 0 # current index of the reference path
        self.ref_speed = 6
        self.L = self.shape[2]

        self.ws = 0.1  # weight of state error
        self.wu = 0.1  # weight of control error
        self.max_speed = np.array([ [10], [1.0] ])
        self.acce_bound = np.array([ [1], [0.1] ]) * self.sample_time 
        self.iter_num = 1

        self.scaling = 10
        self.problem_define()

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
        state_pre_array, ref_traj_list, self.cur_index = self.pre_process(robot_state, self.ref_path_list, self.cur_index, self.ref_speed)

        self.para_ref_s.value = np.hstack(ref_traj_list)[0:3, :]
        self.para_ref_speed.value = self.ref_speed

        self.assign_state_parameter(state_pre_array, self.cur_vel_array)

        nom_s, nom_u = self.iterative_solve()

        velocity = nom_u[:, 0:1]

        velocity[0, 0] = velocity[0, 0] / self.scaling
        velocity[1, 0] = - velocity[1, 0]

        if abs(velocity[1, 0]) < 0.005:
            velocity[1, 0] = 0

        if self.cur_index == len(self.ref_path_list) - 1:
            velocity[0, 0] = 0
            velocity[1, 0] = 0

        "*** YOUR CODE END HERE ***"

        return velocity


    r"""
     You can define your own metohds blow for your planner
    """

    "*** YOUR CODE STARTS HERE ***"

    def problem_define(self):
        
        cost = 0
        constraints = []

        self.indep_s = cp.Variable((3, self.T+1), name='state')
        self.indep_u = cp.Variable((2, self.T), name='vel')

        self.para_s = cp.Parameter((3, self.T+1), name='para_state')
        self.para_u = cp.Parameter((2, self.T), name='para_vel')

        self.para_ref_s = cp.Parameter((3, self.T+1), name='para_ref_state')
        self.para_ref_speed = cp.Parameter(name='para_ref_state')

        self.para_A_list = [ cp.Parameter((3, 3), name='para_A_'+str(t)) for t in range(self.T)]
        self.para_B_list = [ cp.Parameter((3, 2), name='para_B_'+str(t)) for t in range(self.T)]
        self.para_C_list = [ cp.Parameter((3, 1), name='para_C_'+str(t)) for t in range(self.T)]

        cost += self.C0_cost()

        constraints += self.dynamics_constraint()
        constraints += self.bound_su_constraints()

        self.prob = cp.Problem(cp.Minimize(cost), constraints)


    def iterative_solve(self):

        for i in range(self.iter_num):
            
            self.prob.solve(solver=cp.ECOS, verbose=False)
        
            if self.prob.status == cp.OPTIMAL:
                nom_s = self.indep_s.value
                nom_u = self.indep_u.value

            else:
                print('No update of state and control vector')
                
                nom_s = self.para_s.value
                nom_u = self.para_u.value
            
        
            self.assign_state_parameter(nom_s, nom_u)

            self.cur_vel_array = nom_u

        return nom_s, nom_u




    def C0_cost(self):

        diff_s = (self.indep_s - self.para_ref_s)
        diff_u = (self.indep_u[0, :] - self.para_ref_speed)

        L1_norm = cp.norm(self.indep_u[1, :], 1)

        return self.ws * cp.sum_squares(diff_s) + self.wu * cp.sum_squares(diff_u) + 10*L1_norm


    def dynamics_constraint(self):

    
        temp_s1_list = []

        for t in range(self.T):
            indep_st = self.indep_s[:, t:t+1]
            indep_ut = self.indep_u[:, t:t+1]

            ## dynamic constraints
            A = self.para_A_list[t]
            B = self.para_B_list[t]
            C = self.para_C_list[t]
            
            temp_s1_list.append(A @ indep_st + B @ indep_ut + C)
        
        constraints = [ self.indep_s[:, 1:] == cp.hstack(temp_s1_list) ]

        return constraints


    def bound_su_constraints(self):

        constraints = []

        constraints += [ cp.abs(self.indep_u[:, 1:] - self.indep_u[:, :-1] ) <= self.acce_bound ]  # constraints on speed accelerate
        constraints += [ cp.abs(self.indep_u) <= self.max_speed]
        constraints += [ self.indep_s[:, 0:1] == self.para_s[:, 0:1] ]

        return constraints


    def pre_process(self, state, ref_path, cur_index, ref_speed, **kwargs):
        # find closest points 
        min_dis, min_index = self.closest_point(state, ref_path, cur_index, **kwargs)

        # predict the state list and find the reference points list
        cur_state = state
        traj_point = ref_path[min_index]

        ref_traj_list = [ traj_point ]
        state_pre_list = [cur_state]

        for i in range(self.T):
            cur_state = self.motion_predict_model(cur_state, self.cur_vel_array[:, i:i+1], self.L, self.sample_time)
            state_pre_list.append(cur_state)

            move_len = ref_speed * self.sample_time
            traj_point, cur_index = self.inter_point(traj_point, ref_path, cur_index, move_len)

            diff = traj_point[2, 0] - cur_state[2, 0]
            traj_point[2, 0] = cur_state[2, 0] + motion_planner.wraptopi(diff)
            ref_traj_list.append( traj_point )

        state_pre_array = np.hstack(state_pre_list)

        return state_pre_array, ref_traj_list, min_index


    def closest_point(self, state, ref_path, start_ind, threshold=0.1, ind_range=10, **kwargs):
        
        min_dis = inf
        min_ind = start_ind
    
        for i, waypoint in enumerate(ref_path[start_ind:start_ind+ind_range]):
            dis = motion_planner.distance(state[0:2], waypoint[0:2])
            if dis < min_dis:
                min_dis = dis
                min_ind = start_ind + i
                if dis < threshold: break
                    
        return min_dis, min_ind


    def assign_state_parameter(self, nom_s, nom_u):

        self.para_s.value = nom_s
        self.para_u.value = nom_u
        
        for t in range(self.T):
            nom_st = nom_s[:, t:t+1]
            nom_ut = nom_u[:, t:t+1]
            
            A, B, C = self.linear_ackermann_model(nom_st, nom_ut, self.sample_time, self.L)

            self.para_A_list[t].value = A
            self.para_B_list[t].value = B
            self.para_C_list[t].value = C


    def linear_ackermann_model(self, nom_state, nom_u, dt, L):
        
        phi = nom_state[2, 0]
        v = nom_u[0, 0]
        psi = nom_u[1, 0]

        A = np.array([ [1, 0, -v * dt * sin(phi)], [0, 1, v * dt * cos(phi)], [0, 0, 1] ])

        B = np.array([ [cos(phi)*dt, 0], [sin(phi)*dt, 0], 
                        [ tan(psi)*dt / L, v*dt/(L * (cos(psi))**2 ) ] ])

        C = np.array([ [ phi*v*sin(phi)*dt ], [ -phi*v*cos(phi)*dt ], 
                        [ -psi * v*dt / ( L * (cos(psi))**2) ]])

        return A, B, C

    
    def motion_predict_model(self, car_state, vel, wheel_base, sample_time):

        assert car_state.shape == (3, 1) and vel.shape == (2, 1) 

        phi = car_state[2, 0]

        v = vel[0, 0]
        psi = vel[1, 0]

        ds = np.array([ [v*cos(phi)], [v*sin(phi)], [ v*tan(psi) / wheel_base ] ])  
    
        next_state = car_state + ds * sample_time

        return next_state

    def inter_point(self, traj_point, ref_path, cur_ind, length):

        circle = np.squeeze(traj_point[0:2])
        new_traj_point = np.copy(traj_point)

        while True:

            if cur_ind+1 > len(ref_path) - 1:
                
                end_point = ref_path[-1]
                end_point[2] = motion_planner.wraptopi(end_point[2])

                return end_point, cur_ind
            
            cur_point = ref_path[cur_ind]
            next_point = ref_path[cur_ind + 1]

            segment = [np.squeeze(cur_point[0:2]) , np.squeeze(next_point[0:2])]
            int_point = self.range_cir_seg(circle, length, segment)

            if int_point is None:
                cur_ind = cur_ind + 1
            else:
                diff = motion_planner.wraptopi(next_point[2, 0] - cur_point[2, 0])
                theta = motion_planner.wraptopi(cur_point[2, 0] + diff / 2 )
                new_traj_point[0:2, 0] = int_point[:]
                new_traj_point[2, 0] = theta
                
                return new_traj_point, cur_ind

    def range_cir_seg(self, circle, r, segment):
        
        assert circle.shape == (2,) and segment[0].shape == (2,) and segment[1].shape == (2,)

        sp = segment[0]
        ep = segment[1]

        d = ep - sp

        if np.linalg.norm(d) == 0:
            return None

        # if d.all() == 0:
        #     return None

        f = sp - circle

        a = d @ d
        b = 2* f@d
        c = f@f - r ** 2

        discriminant = b**2 - 4 * a * c

        if discriminant < 0:
            return None
        else:
            
            t1 = (-b - sqrt(discriminant)) / (2*a)
            t2 = (-b + sqrt(discriminant)) / (2*a)
  
            if t2 >= 0 and t2 <=1:
                int_point = sp + t2 * d
                return int_point

            return None

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
        
    "*** YOUR CODE END HERE ***"



    




    










