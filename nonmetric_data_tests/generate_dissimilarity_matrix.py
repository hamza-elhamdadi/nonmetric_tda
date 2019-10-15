###############################################################################################################################
#                                     Generate Dissimilarity Matrix given a data set                                          #
###############################################################################################################################

import math
import numpy as np
import sys

# Read in data

data = []

file = open('dataset.txt', 'r')
file_2 = open('dissimilarity_matrix.txt', 'w')

content = file.readlines()

for line in content:
    words = line.split(' ')
    data.append([float(words[0]), float(words[1])])

###############################################################################################################################
#                                                        Functions                                                            #
###############################################################################################################################

# calculate the distance between two points

def distance(p0, p1):
    temp_1 = p1[0]-p0[0]
    temp_2 = p1[1]-p0[1]
    temp_1 = temp_1*temp_1
    temp_2 = temp_2*temp_2
    return math.sqrt(temp_1 + temp_2)

# calculate the nonmetric distance for a given ij element of the dissimilarity matrix

def non_met_distance(x, y, x_k, y_k):
    numer = distance(x,y)
    denom = max([x_k,y_k])
    return numer/denom

# create the dissimilarity matrix

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
    sorted_matrix = []

    for i in range(0, len(mat[0])):
        sorted_row = np.sort(mat[i])
        sorted_matrix.append(sorted_row)
    
    for i in range(0, len(mat[0])):
        current_line = []

        for j in range(0, len(mat[0])):
            current_line.append(non_met_distance(data[i], data[j], sorted_matrix[i][k+1], sorted_matrix[j][k+1]))
        
        nonmetric_dissimilarities.append(current_line)
    
    return np.asanyarray(nonmetric_dissimilarities)

###############################################################################################################################
#                                                     Data Manipulation                                                       #
###############################################################################################################################

#create the dissimilarity matrix for data

mat = dissim_matrix(data)

# Request the user to enter a k-value for the nonmetric matrix mapping

print("Please enter a k-value smaller than 10 to map the data points into a non-metric space (k = 0 will keep the matrix in a metric space)")
k_string = raw_input()
if(int(k_string) > 10):
    print("You entered an invalid k-value. Aborting program.")
    sys.exit()
else:
    k = int(k_string)

if k == 0:
    non_met_mat = mat
else:
    non_met_mat = metric_to_nonmetric(data, mat, k)

for line in non_met_mat:
    string = ""
    for i in line:
        string += str(i) + ' '
    file_2.write(string)
    file_2.write('\n')