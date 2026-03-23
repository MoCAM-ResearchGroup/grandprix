"""
Race data logger — no ROS dependency.

Quickstart: add the following to your motion_planner.py

    from llm_analysis.logger import RaceLogger

    class motion_planner:
        def __init__(self, shape, ref_path_list):
            self.logger = RaceLogger()
            ...

        def calculate_velocity(self, robot_state, obstacle_list):
            ...
            self.logger.log(robot_state, obstacle_list, throttle, steer, brake)
            return control

        def __del__(self):
            self.logger.save("race_log.csv")

Then analyze with:
    python llm_analysis/analyze.py race_log.csv
"""

import csv
import math
import time
from pathlib import Path


class RaceLogger:
    """Records per-step race data to a CSV file."""

    FIELDS = [
        "timestamp",
        "x", "y", "theta",
        "throttle", "steer", "brake",
        "num_obstacles",
        "min_obstacle_dist",
    ]

    def __init__(self):
        self.records: list[dict] = []
        self.start_time = time.time()

    def log(
        self,
        robot_state,
        obstacle_list,
        throttle: float,
        steer: float,
        brake: float = 0.0,
    ):
        """
        Record one control step.

        Args:
            robot_state:   (3, 1) numpy array  [x, y, theta]
            obstacle_list: list of (3, 1) arrays [x, y, theta]
            throttle:      float in [0, 1]
            steer:         float in [-1, 1]
            brake:         float in [0, 1]
        """
        ts = time.time() - self.start_time
        x = float(robot_state[0])
        y = float(robot_state[1])
        theta = float(robot_state[2])

        num_obstacles = len(obstacle_list)
        min_dist = _nearest_obstacle_dist(x, y, obstacle_list)

        self.records.append(
            {
                "timestamp": round(ts, 3),
                "x": round(x, 3),
                "y": round(y, 3),
                "theta": round(theta, 4),
                "throttle": round(float(throttle), 4),
                "steer": round(float(steer), 4),
                "brake": round(float(brake), 4),
                "num_obstacles": num_obstacles,
                "min_obstacle_dist": round(min_dist, 3),
            }
        )

    def save(self, filepath: str = "race_log.csv"):
        """Write recorded data to a CSV file."""
        if not self.records:
            print("[RaceLogger] No data to save.")
            return

        path = Path(filepath)
        path.parent.mkdir(parents=True, exist_ok=True)

        with open(path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDS)
            writer.writeheader()
            writer.writerows(self.records)

        duration = self.records[-1]["timestamp"] - self.records[0]["timestamp"]
        print(
            f"[RaceLogger] Saved {len(self.records)} records "
            f"({duration:.1f}s) → {path}"
        )

    def clear(self):
        """Reset the logger for a new run."""
        self.records.clear()
        self.start_time = time.time()


# ---------------------------------------------------------------------------
# helpers
# ---------------------------------------------------------------------------

def _nearest_obstacle_dist(x: float, y: float, obstacle_list) -> float:
    """Euclidean distance to the nearest obstacle centre. -1 if none."""
    min_dist = float("inf")
    for obs in obstacle_list:
        dx = float(obs[0]) - x
        dy = float(obs[1]) - y
        d = math.sqrt(dx * dx + dy * dy)
        if d < min_dist:
            min_dist = d
    return min_dist if min_dist != float("inf") else -1.0
