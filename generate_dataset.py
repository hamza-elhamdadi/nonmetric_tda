###############################################################################################################################
#                                                  Generate Data Sets                                                         #
###############################################################################################################################

# Necessary imports

import math
import operator as op
import numpy as np
import sys

###############################################################################################################################
#                                                   Useful Functions                                                          #
###############################################################################################################################

# Euclidean distance between two points

def distance(p0, p1):
    temp_1 = p1[0]-p0[0]
    temp_2 = p1[1]-p0[1]
    temp_1 = temp_1*temp_1
    temp_2 = temp_2*temp_2
    return math.sqrt(temp_1 + temp_2)

# Convert Euclidean to non-metric distance given a certain k

def non_met_distance(x, y, x_k, y_k):
    numer = distance(x,y)
    denom = max([x_k,y_k])
    return numer/denom

# create the metric dissimilarity matrix

def dissim_matrix(data):
    dissimilarities = []

    for i in range(0,len(data)):
        current_line = []

        for j in range(0,len(data)):
            current_line.append(distance(data[i],data[j]))
        
        dissimilarities.append(current_line)

    return np.asanyarray(dissimilarities)

# map the metric dissimilarity matrix to a non-metric space

def metric_to_nonmetric(data, mat, k):
    nonmetric_dissimilarities = []
    
    for i in range(0, len(mat[0])):
        current_line = []
        sorted_row = np.sort(mat[i])

        for j in range(0, len(mat[0])):
            sorted_col = np.sort(mat[j])

            current_line.append(non_met_distance(data[i], data[j], sorted_row[k+1], sorted_col[k+1]))
        
        nonmetric_dissimilarities.append(current_line)
    
    return np.asanyarray(nonmetric_dissimilarities)

###############################################################################################################################
#                                                      Make the data                                                          #
###############################################################################################################################

data_set = []
num_data_points = []
radii = []
randomness_vals_x = []
randomness_vals_y = []


# Request user input for the number of circles

print("Please enter the number of circles (fewer than or equal ten) you would like in your data set")
if int(raw_input()) <= 10:
    num_circles = int(raw_input())
else:
    print("You entered an invalid number of circles. Aborting program.")
    sys.exit()

# Request user input for the number of data points in each of the circles

for i in range(num_circles):
    print("Please enter the number of data points (fewer than or equal to 1000) you would like in circle " + str(i+1))
    if int(raw_input()) <= 1000:
        num_data_points.add(int(raw_input()))
    else:
        print("You entered an invalid number of data points. Aborting program.")
        sys.exit()

# Request user for range of randomness they would like to enter

print("Please enter the range of randomness (smaller than or equal to 5) you would like to add to all of the points in the form (x y)")
rand_range_start = raw_input()[1]
rand_range_end = raw_input()[-1]
if int(rand_range_start) <= 5 and int(rand_range_end) <= 5 and int(rand_range_start) > 0 and int(rand_range_end) > 0:
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
    if int(raw_input()) <= 10:
        radii.add(int(raw_input()))
    else:
        print("You entered an invalid radius. Aborting program.")
        sys.exit()    

# Generate random values for each of the circles

for i in range(num_circles):
    randomness_vals_x.add([np.random.uniform(rand_range_start, rand_range_end) for x in range(0,num_data_points[i]+1)])
    randomness_vals_y.add([np.random.uniform(rand_range_start, rand_range_end) for y in range(0,num_data_points[i]+1)])

for i in range(num_circles):
    if i > 0:
        center = radii[i-1]+radii[i]
    data_set.add([(math.cos(2*np.pi/num_data_points[i]*x)*radii[i]+center+val_x_1[x],math.sin(2*np.pi/num_data_points[i]*x)*radii[i]+randomness_vals_y[i][x]) for x in range(0, num_data_points[i]+1)])
