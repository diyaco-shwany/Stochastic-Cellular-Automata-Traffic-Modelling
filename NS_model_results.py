# -*- coding: utf-8 -*-

import numpy as np
import random as rand

VMAX= 5
LENGTH = 55
CARS = 49
ITERATIONS = 40
def acceleration(velocity_1, position_1, position_2):

    if position_2 - position_1 > velocity_1 + 1:
        if velocity_1 < VMAX:
            velocity_1 = velocity_1 + 1
            #print(velocity_1)
    return velocity_1

def deceleration(velocity_1, position_1, position_2):

    if position_2 - position_1 <= velocity_1:
        #print(position_2 - position_1)
        velocity_1 = (position_2 - position_1) - 1
        #print(velocity_1)
    return velocity_1

def random(vehicle_v, v_max = VMAX):

    #probability = rand.uniform(0,1)
    #if probability > 0.8:
        #if vehicle_v > 0:
            #return vehicle_v - 1
        #else:
            #return vehicle_v
    #else:
        #return vehicle_v
    probability = rand.randint(0,1)

    if probability == 1:

        if vehicle_v > 0:
            return vehicle_v -1
        else:
            return vehicle_v
    else:
        return vehicle_v

def car_moves(velocity, position):

    position += velocity

    return position

def car():
    velocity = rand.randint(2, VMAX - 1)
    position = rand.randint(0, LENGTH - 1)

    return (position, velocity)

def road(velocity_all, position_all):
    #print(position_all)
    road = []
    for i in range(LENGTH):
        road.append('.')
    count_0 = -1
    for i in position_all:
        count_0 += 1

        road[i] = velocity_all[count_0]


    print(*road, sep = "")
    return road


def main():
    velocity_all = []
    position_all = []
    for i in range(CARS):
        position, velocity = car()
        while True:
            if position in position_all:
                position, velocity = car()
            else:

                break


        position_all.append(position)
        velocity_all.append(velocity)


    position_all.sort(reverse=True)

    road(velocity_all, position_all)

    indices = []
    counter_1 = 0
    counter_2 = 0
    counter_3 = 0
    while counter_1 < ITERATIONS:

        counter_0 = -1
        position_front = 2 * LENGTH

        for i in position_all:
            counter_0 += 1

            velocity_1 = acceleration(velocity_all[counter_0], i, position_front)
            velocity_1 = deceleration(velocity_1, i, position_front)
            velocity_1 = random(velocity_1)

            position_front = position_all[counter_0]

            velocity_all[counter_0] = velocity_1

        counter_0 = -1
        for i in position_all:
            counter_0 += 1

            new_position = car_moves(velocity_all[counter_0], position_all[counter_0])
            position_front = new_position
            if new_position > LENGTH - 1:
                indices.append(counter_0)
                #position_all.append(new_position - LENGTH)
                #velocity_all.append(velocity_1)
            else:
                position_all[counter_0] = new_position
        for i in indices:

            position_all.remove(position_all[i])
            del velocity_all[i]


        road_test = road(velocity_all, position_all)
        if isinstance(road_test[33], int) == True:
            counter_2 += 1
            if road_test[33] > 0:
                counter_3 += 1
        counter_1 += 1
        if counter_1 == ITERATIONS:
            print("car density is:", counter_2/ITERATIONS)
            print("flow rate is:", counter_3/ITERATIONS)
        indices.clear()



main()