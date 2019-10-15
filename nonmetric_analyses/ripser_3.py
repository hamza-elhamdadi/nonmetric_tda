###############################################################################################################################
#                                       Dissimilarity Matrix for Non-metric space                                             #
###############################################################################################################################

import math
import time
import operator as op
import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

###############################################################################################################################
#                                                        functions                                                            #
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
    
    for i in range(0, len(mat[0])):
        current_line = []
        sorted_row = np.sort(mat[i])

        for j in range(0, len(mat[0])):
            sorted_col = np.sort(mat[j])

            current_line.append(non_met_distance(data[i], data[j], sorted_row[k+1], sorted_col[k+1]))
        
        nonmetric_dissimilarities.append(current_line)
    
    return np.asanyarray(nonmetric_dissimilarities)

###############################################################################################################################
#                                                          data                                                               #
###############################################################################################################################

# number of points in data set, k, and pi

num_points_1 = 50
num_points_2 = 100
k_vals = [i+1 for i in range(10)]
pi = np.pi

# list of random values to be added the x and y values for each point in the data set

val_x_1=[np.random.uniform(0, 1) for x in range(0,num_points_1+1)]
val_y_1=[np.random.uniform(0, 1) for x in range(0,num_points_1+1)]

val_x_2=[np.random.uniform(0, 1) for x in range(0,num_points_2+1)]
val_y_2=[np.random.uniform(0, 1) for x in range(0,num_points_2+1)]

# the actual data set we will be working with

data_1 = [(math.cos(2*pi/num_points_1*x)*5+val_x_1[x],math.sin(2*pi/num_points_1*x)*5+val_y_1[x]) for x in range(0, num_points_1+1)]
data_2 = [(math.cos(2*pi/num_points_2*x)*2+7+val_x_2[x],math.sin(2*pi/num_points_2*x)*2+val_y_2[x]) for x in range(0, num_points_2+1)]

data = data_1 + data_2

# the separated lists of x and y values to be used by the plt.scatter method later on

data_x=map(op.itemgetter(0),data)
data_y=map(op.itemgetter(1),data)



###############################################################################################################################
#                                                   data manipulation                                                         #
###############################################################################################################################

# create the dissimilarity matrix for the metric space given the data array

dissimilarities = dissim_matrix(data)

# map the dissimilarity matrix to a nonmetric space

nonmetric_dissimilarities = [metric_to_nonmetric(data, dissimilarities, k) for k in k_vals]

###############################################################################################################################
#                                                        diagrams                                                             #
###############################################################################################################################

# open a file to write the persistence diagrams

file_1 = open("./persistence_diagrams/persistence_diagram_metric.txt", "w+")
file_2 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_1.txt", "w+")
file_3 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_2.txt", "w+")
file_4 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_3.txt", "w+")
file_5 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_4.txt", "w+")
file_6 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_5.txt", "w+")
file_7 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_6.txt", "w+")
file_8 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_7.txt", "w+")
file_9 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_8.txt", "w+")
file_10 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_9.txt", "w+")
file_11 = open("./persistence_diagrams/persistence_diagram_nonmetric_k_10.txt", "w+")

# save the scatter plot of our data set for reference to a png file

plt.scatter(data_x,data_y,np.pi*3)
plt.savefig('data_scatterplot.png')
plt.clf()

print('Scatterplot saved as data_scatterplot.png')

# create the persistence diagram for the metric space and display it

diagrams_1 = ripser(dissimilarities, distance_matrix = True)['dgms']

# write the first persistence diagram as a list of points to a txt file

for i in list(diagrams_1[0]):
    file_1.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_1[1]):
    file_1.write(str(i[0]) + " " + str(i[1]) + "\n")

# allow the first diagram to stay before the second diagram is shown

time.sleep(0)

# create the persistence diagram and display it

diagrams_2 = [ripser(nonmetric_dissimilarities[i], distance_matrix = True)['dgms'] for i in range(len(nonmetric_dissimilarities))]

# write the other persistence diagram as a list of points to a txt file

for i in list(diagrams_2[0][0]):
    file_2.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[0][1]):
    file_2.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[1][0]):
    file_3.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[1][1]):
    file_3.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[2][0]):
    file_4.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[2][1]):
    file_4.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[3][0]):
    file_5.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[3][1]):
    file_5.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[4][0]):
    file_6.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[4][1]):
    file_6.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[5][0]):
    file_7.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[5][1]):
    file_7.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[6][0]):
    file_8.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[6][1]):
    file_8.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[7][0]):
    file_9.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[7][1]):
    file_9.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[8][0]):
    file_10.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[8][1]):
    file_10.write(str(i[0]) + " " + str(i[1]) + "\n")

for i in list(diagrams_2[9][0]):
    file_11.write(str(i[0]) + " " + str(i[1]) + "\n")
for i in list(diagrams_2[9][1]):
    file_11.write(str(i[0]) + " " + str(i[1]) + "\n")