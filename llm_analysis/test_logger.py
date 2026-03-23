import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import numpy as np
from llm_analysis.logger import RaceLogger

logger = RaceLogger()

for i in range(50):
    robot_state = np.array([[980.0 + i * 0.5], [581.0], [1.57]])
    obstacle_list = [
        np.array([[990.0], [582.0], [0.0]]),
        np.array([[995.0], [580.0], [0.5]]),
    ]
    throttle = 0.6 + 0.1 * (i % 3)
    steer = 0.05 * ((-1) ** i)
    brake = 0.0
    logger.log(robot_state, obstacle_list, throttle, steer, brake)

logger.save("/tmp/test_race_log.csv")

print("前3行内容:")
with open("/tmp/test_race_log.csv") as f:
    for j, line in enumerate(f):
        print(line, end="")
        if j >= 3:
            break
