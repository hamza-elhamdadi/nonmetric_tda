###############################################################################################################################
#                                          Dissimilarity Matrix for Metric Space                                              #
###############################################################################################################################

import math
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

###############################################################################################################################
#                                                          data                                                               #
###############################################################################################################################

# number of points in our data set

num_points = 15

# simplifying math.pi to pi

pi = np.pi

# list of random values to be added the x and y values for each point in the data set

val_x=[np.random.randint(low=0, high=3) for x in range(0,num_points+1)]
val_y=[np.random.randint(low=0, high=3) for x in range(0,num_points+1)]

# the actual data set we will be working with

data = [(math.cos(2*pi/num_points*x)*5+val_x[x],math.sin(2*pi/num_points*x)*5+val_y[x]) for x in range(0, num_points+1)]

# values for the dissimilarity matrix we will create later on

dissimilarities = []

# the separated lists of x and y values to be used by the plt.scatter method later on

data_x=[math.cos(2*pi/num_points*x)*5+val_x[x] for x in range(0,num_points+1)]
data_y=[math.sin(2*pi/num_points*x)*5+val_y[x] for x in range(0,num_points+1)]

###############################################################################################################################
#                                                   data manipulation                                                         #
###############################################################################################################################

# save the scatter plot of our data set for reference to a png file

plt.scatter(data_x,data_y,np.pi*3)
plt.savefig('data_scatterplot.png')

print('Scatterplot saved as data_scatterplot.png')

# create the dissimilarity matrix

for i in range(0,len(data)-1):
    current_line = []
    for j in range(0,len(data)-1):
        current_line.append(distance(data[i],data[j]))
    dissimilarities.append(current_line)

# make the dissimilarity matrix into an ndarray

dissimilarities = np.asanyarray(dissimilarities)

# create the persistence diagram and display it

diagrams = ripser(dissimilarities, distance_matrix = True)['dgms']

plot_diagrams(diagrams, show = True)

