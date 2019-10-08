###############################################################################################################################
#                                        Rebuild Data Set given Dissimilarity Matrix                                          #
###############################################################################################################################

from sklearn.manifold import MDS
import operator as op
import numpy as np
import matplotlib.pyplot as plt

mat = []

file = open('dissimilarity_matrix.txt', 'r')

content = file.readlines()

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

embedding = MDS(n_components=2,dissimilarity='precomputed')

data = embedding.fit_transform(new_mat)

data_x=map(op.itemgetter(0),data)
data_y=map(op.itemgetter(1),data)

plt.scatter(data_x,data_y,np.pi*3)
plt.savefig("new_dataset.png")
plt.show()
