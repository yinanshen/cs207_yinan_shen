mport numpy as np 

def read_in_data(filename):
    raw_data = open(filename, "r+")
    radius_list = raw_data.read().strip().split('\n')
    radius_float_list = [float(radius) for radius in radius_list]
    return radius_float_list

def area_of_circle(radius):
    circle_area = np.pi*radius**2
    return circle_area

def my_ave(radius_float_list):
    area_list = [area_of_circle(radius) for radius in radius_float_list]
    mean_area = sum(area_list) / len(area_list)
    return mean_area

get_radius_float_list = read_in_data('circles.txt')
get_mean_area = my_ave(get_radius_float_list)
print('Myavg : ', get_mean_area)
