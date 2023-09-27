import numpy as np

class motion_planner:
    def __init__(self, shape, ref_path_list):

        r"""
        @param shape: list of the vehicle shape [length, width, wheelbase, width_wheelbase] 
        @param ref_path_list: the reference path that the vehicle should follow
        """

        self.ref_path_list = ref_path_list
        self.shape = shape
        self.velocity = np.zeros((2, 1))

        "*** YOUR CODE STARTS HERE ***"
        # You can define your own instance attributes here

        

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
        

        



        "*** YOUR CODE END HERE ***"


        return velocity


    r"""
     You can define your own metohds blow for your planner
    """

    "*** YOUR CODE STARTS HERE ***"





    "*** YOUR CODE END HERE ***"







    










