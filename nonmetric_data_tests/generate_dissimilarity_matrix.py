###############################################################################################################################
#                                     Generate Dissimilarity Matrix given a data set                                          #
###############################################################################################################################

import math
import numpy as np
import sys

# Read in data

data = []

file = open('data_files/dataset.txt', 'r')
files = [open('data_files/k0_dissimilarity_matrix.txt', 'w'),
         open('data_files/k1_dissimilarity_matrix.txt', 'w'),
         open('data_files/k2_dissimilarity_matrix.txt', 'w'),
         open('data_files/k3_dissimilarity_matrix.txt', 'w'),
         open('data_files/k4_dissimilarity_matrix.txt', 'w'),
         open('data_files/k5_dissimilarity_matrix.txt', 'w'),
         open('data_files/k6_dissimilarity_matrix.txt', 'w'),
         open('data_files/k7_dissimilarity_matrix.txt', 'w'),
         open('data_files/k8_dissimilarity_matrix.txt', 'w')]

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

# sort the rows metric dissimilarity matrix by row

def sort_metric(mat, sorted_matrix):

    for i in range(0, len(mat[0])):
        sorted_row = np.sort(mat[i])
        sorted_matrix.append(sorted_row)

# map the metric dissimilarity matrix to a non-metric space

def metric_to_nonmetric(data, mat, sorted_matrix, k):
    nonmetric_dissimilarities = []
    
    for i in range(0, len(mat[0])):
        current_line = []

        for j in range(0, len(mat[0])):
            current_line.append(non_met_distance(data[i], data[j], sorted_matrix[i][k+1], sorted_matrix[j][k+1]))
        
        nonmetric_dissimilarities.append(current_line)
    
    return np.asanyarray(nonmetric_dissimilarities)

###############################################################################################################################
#                                                     Data Manipulation                                                       #
###############################################################################################################################

# create the dissimilarity matrix for data

mat = dissim_matrix(data)

# fill out the metric data file

k = 0

sorted_matrix = []
sort_metric(mat, sorted_matrix)

for curr_file in files:
    if k == 0:
        for line in mat:
            string = ""
            for i in line:
                string += str(i) + ' '
            curr_file.write(string)
            curr_file.write('\n')
        k += 1
    else:
        non_met_mat = metric_to_nonmetric(data, mat, sorted_matrix, k)
        k += 1

        for line in non_met_mat:
            string = ""
            for i in line:
                string += str(i) + ' '
            curr_file.write(string)
            curr_file.write('\n')
