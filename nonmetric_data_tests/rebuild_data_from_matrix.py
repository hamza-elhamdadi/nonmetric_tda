###############################################################################################################################
#                                        Rebuild Data Set given Dissimilarity Matrix                                          #
###############################################################################################################################

from sklearn.manifold import MDS
import operator as op
import numpy as np
import subprocess as sp
import matplotlib.pyplot as plt

sp.call(['mkdir', 'data_files/intermediate_data'])

color_sequence = []

files = [open('data_files/k0_dissimilarity_matrix.txt', 'r'),
         open('data_files/k1_dissimilarity_matrix.txt', 'r'),
         open('data_files/k2_dissimilarity_matrix.txt', 'r'),
         open('data_files/k3_dissimilarity_matrix.txt', 'r'),
         open('data_files/k4_dissimilarity_matrix.txt', 'r'),
         open('data_files/k5_dissimilarity_matrix.txt', 'r'),
         open('data_files/k6_dissimilarity_matrix.txt', 'r'),
         open('data_files/k7_dissimilarity_matrix.txt', 'r'),
         open('data_files/k8_dissimilarity_matrix.txt', 'r')]
data_files = [open('data_files/intermediate_data/k0_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k1_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k2_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k3_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k4_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k5_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k6_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k7_remapped_dataset.txt', 'w'),
              open('data_files/intermediate_data/k8_remapped_dataset.txt', 'w')]
color_file = open('data_files/data_colors.txt', 'r')

color_content = color_file.readlines()

for line in color_content:
    vals = line.split(' ')
    for x in range(int(vals[1])+1):
        color_sequence.append(vals[0])

i = 1

for file in files:
    content = file.readlines()

    mat = []
    plt.clf()

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

    for j in data:
        data_files[i-1].write(str(j[0]) + ' ' + str(j[1]) + '\n')

    data_x=map(op.itemgetter(0),data)
    data_y=map(op.itemgetter(1),data)

    filepath = "pictures/new_dataset" + str(i)
    i += 1

    plt.scatter(data_x,data_y,np.pi*3, c = color_sequence, edgecolors = color_sequence)
    plt.savefig(filepath)
