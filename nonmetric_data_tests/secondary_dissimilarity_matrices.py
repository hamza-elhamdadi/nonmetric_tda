###############################################################################################################################
#                                     Generate Dissimilarity Matrix given a data set                                          #
###############################################################################################################################

import math
import numpy as np
import sys
import subprocess as sp

# Read in data

sp.call(['mkdir', 'data_files/secondary_dissimilarity_matrices'])

matrix_files = [open('data_files/k0_dissimilarity_matrix.txt', 'r'),
            open('data_files/k1_dissimilarity_matrix.txt', 'r'),
            open('data_files/k2_dissimilarity_matrix.txt', 'r'),
            open('data_files/k3_dissimilarity_matrix.txt', 'r'),
            open('data_files/k4_dissimilarity_matrix.txt', 'r'),
            open('data_files/k5_dissimilarity_matrix.txt', 'r'),
            open('data_files/k6_dissimilarity_matrix.txt', 'r'),
            open('data_files/k7_dissimilarity_matrix.txt', 'r'),
            open('data_files/k8_dissimilarity_matrix.txt', 'r')]

files = [open('data_files/intermediate_data/k0_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k1_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k2_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k3_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k4_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k5_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k6_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k7_remapped_dataset.txt', 'r'),
         open('data_files/intermediate_data/k8_remapped_dataset.txt', 'r')]

datasets = []
old_matrices = []
new_matrices = []

for file in files:
    content = file.readlines()
    data = []

    for line in content:
        words = line.split(' ')
        data.append([float(words[0]), float(words[1])])
    datasets.append(data)
    
for file in matrix_files:
    content = file.readlines()
    mat = []

    for line in content:
        row = []
        words = line.split()
        for num in words:
            try:
                row.append(float(num))
            except ValueError:
                print "Not a float",num
        mat.append(row)
    new_mat = np.asmatrix(mat)

    old_matrices.append(new_mat)

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

# create the dissimilarity matrix

def dissim_matrix(data):
    dissimilarities = []

    for i in range(0,len(data)):
        current_line = []

        for j in range(0,len(data)):
            current_line.append(distance(data[i],data[j]))
        
        dissimilarities.append(current_line)

    return np.asmatrix(dissimilarities)

###############################################################################################################################
#                                                   Data Manipulation                                                         #
###############################################################################################################################

for data in datasets:
    dmat = dissim_matrix(data)
    new_matrices.append(dmat)

# for i in range(len(datasets)):
#     norm_1 = np.linalg.norm(old_matrices[i])
#     norm_2 = np.linalg.norm(new_matrices[i])

#     print("k = " + str(i) + " prior to embedding: norm = " + str(norm_1) + " after embedding: norm = " + str(norm_2))

for i in range(len(datasets)):
    mat = np.subtract(old_matrices[i],new_matrices[i])

    norm = np.linalg.norm(mat)

    print("k = " + str(i) + " subtracted norm = " + str(norm))