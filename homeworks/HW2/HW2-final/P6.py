# P6

import numpy as np
import time

def timer(the_function):
    def timer_inner(*args):
        time_begin = time.time()
        the_function(*args)
        time_end = time.time()
        time_elapsed_total = time_end - time_begin
        averaged_time_elapsed = time_elapsed_total / test_how_many_times
        print("The time cost is", averaged_time_elapsed)
        print('')
    return timer_inner

def read_in_data(filename):
    raw_data = open(filename, "r+")
    radius_list = raw_data.read().strip().split('\n')
    radius_float_list = [float(radius) for radius in radius_list]
    return radius_float_list


# My average def
## Preallocate
area_list = [0.0] * len(get_radius_float_list)
## For competition
@timer
def my_ave(get_radius_float_list):
    for count in range(test_how_many_times - 1):
        for index in range(len(get_radius_float_list)):
            area_list[index] = np.pi * get_radius_float_list[index]**2
        my_mean_area = sum(area_list) / len(area_list)
    print('The averaged area using my method is', my_mean_area)


# Numpy def
## Preallocate
areas_np = np.zeros(len(get_radius_float_list))
## For competition
@timer
def np_ave(get_radius_float_list):
    for count in range(test_how_many_times - 1):
        areas_np = np.power(get_radius_float_list, 2) * np.pi
        np_mean_area = np.mean(areas_np)
    print('The averaged area using np method is', np_mean_area)


get_radius_float_list = read_in_data('circles.txt')
test_how_many_times = 100
print('The speed test result is given by carrying out', test_how_many_times, 'tests.')
print('')
my_mean = my_ave(get_radius_float_list)
np_mean = np_ave(get_radius_float_list)
