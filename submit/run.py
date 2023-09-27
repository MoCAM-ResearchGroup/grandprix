import ast
from core import core
import argparse

def main(file_name):

    motion_planner = core(file_name)
    motion_planner.publisher()


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('-f', '--file', default='motion_planner_mpc.py')
    args = parser.parse_args()

    main(args.file)
    