#!/usr/bin/env python

# Copyright (c) 2019 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import random
import time


def main():
    

    try:
        
        client = carla.Client('localhost', 2000)
        client.set_timeout(10.0)

        
        world = client.get_world()

        spawn_points = [[-55,0,0.2], [-60,0,0.2], [-65,0,0.2], [-70,0,0.2], [-75,0,0.2], 
                        [-80,0,0.2], [-85,0,0.2], [-90,0,0.2], [-95,0,0.2], 
                        [-55,0,0.2], [-55,5,0.2], [-55,10,0.2], [-55,15,0.2],[-55,20,0.2],
                        [-55,25,0.2], [-55,30,0.2], [-55,35,0.2], 
                        [-95,0,0.2], [-95,5,0.2], [-95,10,0.2], [-95,15,0.2],[-95,20,0.2],
                        [-95,25,0.2], [-95,30,0.2], [-95,35,0.2],
                        [-70,15,0.2], # center
                        [-80,33,0.2], # windows
                        [-85,25,0.2], # windows
                        [-76,21,0.2], # rotate
                        ]


        num_cubes = len(spawn_points)
        bp_list = []
        tf_list = []
        cube_list = []
        print('number of cubes:', num_cubes)

        blueprintsCubes = world.get_blueprint_library().filter("static.prop.cube_red*")
        for i in range(num_cubes):
            
            bp = random.choice(blueprintsCubes)
            bp_list.append(bp)

            tf = carla.Transform(carla.Location(x = spawn_points[i][0], y = spawn_points[i][1], z = spawn_points[i][2]) ,carla.Rotation())
            tf_list.append(tf)

            if i == num_cubes-1:
                tf = carla.Transform(carla.Location(x = spawn_points[i][0], y = spawn_points[i][1], z = spawn_points[i][2]), \
                carla.Rotation(yaw = 30, pitch = 0, roll = 0))
                tf_list.append(tf)

            cube = world.try_spawn_actor(bp, tf)
            cube_list.append(cube)
        
        # spawn_human = [[-90,15,0.2]]
        # num_human = len(spawn_human)
        # bp_list = []
        # tf_list = []
        # human_list = []
        # print('number of humans:', num_human)

        # blueprintsHuman = world.get_blueprint_library().filter("walker.pedestrian.*")
        # for i in range(num_human):
            
        #     bp = random.choice(blueprintsHuman)
        #     bp_list.append(bp)

        #     tf = carla.Transform(carla.Location(x = spawn_human[i][0], y = spawn_human[i][1], z = spawn_human[i][2]) , \
        #     carla.Rotation(yaw = 0, pitch = 0, roll = 0))
        #     tf_list.append(tf)

        #     human = world.try_spawn_actor(bp, tf)
        #     human_list.append(human)

        while(True):
            time.sleep(1)

    finally:

        print('destroying actors')
        client.apply_batch([carla.command.DestroyActor(x) for x in cube_list])
        print('done.')


if __name__ == '__main__':

    main()




        # cube_1 = world.try_spawn_actor(bp[0], transform_1)
        # cube_2 = world.try_spawn_actor(bp[1], transform_2)
        # cube_3 = world.try_spawn_actor(bp[2], transform_3)
        # cube_4 = world.try_spawn_actor(bp[3], transform_4)
        # cube_5 = world.try_spawn_actor(bp[4], transform_5)
        # cube_6 = world.try_spawn_actor(bp[5], transform_6)
        # cube_7 = world.try_spawn_actor(bp[6], transform_7)
        # cube_8 = world.try_spawn_actor(bp[7], transform_8)
        # cube_9 = world.try_spawn_actor(bp[8], transform_9)


        # transform_5 = carla.Transform(carla.Location(x = -68, y = 0, z = 0.2) ,carla.Rotation())
        # transform_6 = carla.Transform(carla.Location(x = -72, y = 0, z = 0.2) ,carla.Rotation())
        # transform_1 = carla.Transform(carla.Location(x = -76, y = 0, z = 0.2) ,carla.Rotation())
        # transform_2 = carla.Transform(carla.Location(x = -80, y = 0, z = 0.2) ,carla.Rotation())
        # transform_3 = carla.Transform(carla.Location(x = -84, y = 0, z = 0.2) ,carla.Rotation())
        # transform_4 = carla.Transform(carla.Location(x = -88, y = 0, z = 0.2) ,carla.Rotation())
        # transform_7 = carla.Transform(carla.Location(x = -64, y = 0, z = 0.2) ,carla.Rotation())
        # transform_8 = carla.Transform(carla.Location(x = -60, y = 0, z = 0.2) ,carla.Rotation())
        # transform_9 = carla.Transform(carla.Location(x = -56, y = 0, z = 0.2) ,carla.Rotation())
        