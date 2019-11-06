###############################################################################################################################
#                                                  Generate Data Sets                                                         #
###############################################################################################################################

# Necessary imports

import math
import operator as op
import numpy as np
import matplotlib.pyplot as plt
from itertools import chain
import sys
import nmf

###############################################################################################################################
#                                                      Make the data                                                          #
###############################################################################################################################

data = []
data_set = []
num_data_points = []
radii = []
pi = np.pi

colors = ['#FF00FF','#469990','#00FF00','#0000FF','#FF0000','#800000','#000075','#e6beff','#fabebe','#FF0000']
color_sequence = []

# Request user input for the number of circles

print("Please enter the number of circles (fewer than or equal ten) you would like in your data set")
str_num_circles = raw_input()
if int(str_num_circles) <= 10:
    num_circles = int(str_num_circles)
else:
    print("You entered an invalid number of circles. Aborting program.")
    sys.exit()

# Request user input for the number of data points in each of the circles

for i in range(num_circles):
    print("Please enter the number of data points (fewer than or equal to 1000) you would like in circle " + str(i+1))
    str_num_data_points = raw_input()
    if int(str_num_data_points) <= 1000:
        num_data_points.append(int(str_num_data_points))
        for j in range(int(str_num_data_points)+1):
            color_sequence.append(colors[i])
    else:
        print("You entered an invalid number of data points. Aborting program.")
        sys.exit()

# Request user for range of randomness they would like to enter

print("Please enter the range of randomness (smaller than or equal to 5) you would like to add to all of the points in the form (x y)")
rand_inputs = raw_input()
rand_range_start = rand_inputs[0]
rand_range_end = rand_inputs[-1]
if int(rand_range_start) <= 5 and int(rand_range_end) <= 5 and int(rand_range_start) >= 0 and int(rand_range_end) >= 0:
    rand_range_start = int(rand_range_start)
    rand_range_end = int(rand_range_end)
    if rand_range_start > rand_range_end:
        rand_range_end *= rand_range_start
        rand_range_start = rand_range_end/rand_range_start
        rand_range_end = rand_range_end/rand_range_start
else:
    print("You entered one or more invalid values. Aborting program.")
    sys.exit()

# Request user for radii for each circle

for i in range(num_circles):
    print("Please enter the radius (smaller than or equal to 10) for circle" + str(i+1))
    curr_radius = raw_input()
    if int(curr_radius) <= 10:
        radii.append(int(curr_radius))
    else:
        print("You entered an invalid radius. Aborting program.")
        sys.exit()    

# Ask the user if they would like to add "dense to sparse" gradients to their data

print("Would you like the data points in your circles to shift from dense to sparse (y/n)?")
inp = raw_input()
if inp == 'y':
    denseToSparse = True
elif inp == 'n':
    denseToSparse = False
else: 
    print("You entered invalid input. Aborting program.")
    sys.exit()

randomness_vals_x = []
randomness_vals_y = []

# Generate random values for each of the circles
for i in range(num_circles):
    randomness_vals_x.append(nmf.rand_vals(rand_range_start, rand_range_end, num_data_points[i]))
    randomness_vals_y.append(nmf.rand_vals(rand_range_start, rand_range_end, num_data_points[i]))

# Generate the data set

center = radii[0]

if(denseToSparse):
    for i in range(num_circles):
        next_set = []
        if i+1 > 0:
            center += radii[i-1]+radii[i]+1
        for x in range(0, num_data_points[i] + 1):
            angle = 2*pi/num_data_points[i]*x
            angle = nmf.dense_angle_to_sparse(angle, pi/4)
            x_val = math.cos(angle)*radii[i]+center+randomness_vals_x[i][x]
            y_val = math.sin(angle)*radii[i]+randomness_vals_y[i][x]
            point = [x_val, y_val]
            next_set.append(point)
        data_set.append(next_set)
else:
    for i in range(num_circles):
        if i+1 > 0:
            center += radii[i-1]+radii[i]+1
        data_set.append([[math.cos(2*pi/num_data_points[i]*x)*radii[i]+center+randomness_vals_x[i][x],math.sin(2*pi/num_data_points[i]*x)*radii[i]+randomness_vals_y[i][x]] for x in range(0, num_data_points[i]+1)])

data = list(chain(*data_set))

file = open("data_files/dataset.txt", "w+")
color_file = open("data_files/data_colors.txt", 'w+')

for i in range(len(num_data_points)):
     color_file.write(colors[i] + ' ' + str(num_data_points[i]) + '\n')

for i in data:
    file.write(str(i[0]) + ' ' + str(i[1]) + '\n')

data_x = map(op.itemgetter(0), data)
data_y = map(op.itemgetter(1), data)

plt.scatter(data_x,data_y,pi*3, c = color_sequence, edgecolors = color_sequence)
plt.savefig("pictures/og_dataset.png")
plt.show()