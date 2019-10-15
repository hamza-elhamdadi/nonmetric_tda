###############################################################################################################################
#                                                        functions                                                            #
###############################################################################################################################

import math
import numpy as np
import matplotlib.pyplot as plt
from ripser import ripser
from persim import plot_diagrams

pi = math.pi

num_points=100

val_x=[np.random.randint(low=0, high=3) for x in range(0,num_points+1)]
val_y=[np.random.randint(low=0, high=3) for x in range(0,num_points+1)]

data_points = [(math.cos(2*pi/num_points*x)*5+val_x[x],math.sin(2*pi/num_points*x)*5+val_y[x]) for x in range(0, num_points+1)]

data_x=[math.cos(2*pi/num_points*x)*5+val_x[x] for x in range(0,num_points+1)]
data_y=[math.sin(2*pi/num_points*x)*5+val_y[x] for x in range(0,num_points+1)]


data = np.asarray(data_points)

diagrams = ripser(data)['dgms']
plot_diagrams(diagrams, show = True)

plt.scatter(data_x, data_y, np.pi*3)
plt.show()