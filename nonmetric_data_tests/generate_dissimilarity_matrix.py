###############################################################################################################################
#                                     Generate Dissimilarity Matrix given a data set                                          #
###############################################################################################################################

import math
import numpy as np
import sys
import nmf
from ripser import ripser
from persim import plot_diagrams

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
#                                                     Data Manipulation                                                       #
###############################################################################################################################

# create the dissimilarity matrix for data

mat = nmf.dissim_matrix(data)

# fill out the metric data file

k = 0

sorted_matrix = []
nmf.sort_metric(mat, sorted_matrix)

for curr_file in files:
    if k == 0:
        diagrams = ripser(mat, distance_matrix = True)['dgms']
        plot_diagrams(diagrams, show = True)

        for line in mat:
            string = ""
            for i in line:
                string += str(i) + ' '
            curr_file.write(string)
            curr_file.write('\n')
        k += 10
    else:
        non_met_mat = nmf.metric_to_nonmetric(data, mat, sorted_matrix, k)
        diagrams = ripser(non_met_mat, distance_matrix = True)['dgms']
        plot_diagrams(diagrams, show = True)

        k += 10

        for line in non_met_mat:
            string = ""
            for i in line:
                string += str(i) + ' '
            curr_file.write(string)
            curr_file.write('\n')
