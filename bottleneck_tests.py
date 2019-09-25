import subprocess as sp

sp.call(['python', 'ripser_3.py'])

sp.call(['touch', 'bottleneck_values.txt'])

cmd_3 = 'echo "" >> bottleneck_values.txt'

for i in range(10):
    cmd_1 = 'echo "Metric compared to k = ' + str(i+1) +'" >> bottleneck_values.txt'
    cmd_2 = './hera/geom_bottleneck/build/bottleneck_dist ./persistence_diagrams/persistence_diagram_metric.txt ./persistence_diagrams/persistence_diagram_nonmetric_k_' + str(i+1) + '.txt >> bottleneck_values.txt'
    sp.call(['sh', '-c', cmd_1])
    sp.call(['sh', '-c', cmd_2])
    sp.call(['sh', '-c', cmd_3])

for i in range(10):
    for j in range(i+1,10):
        cmd_1 = 'echo "k = ' + str(i+1) + ' compared to k = ' + str(j+1) +'" >> bottleneck_values.txt'
        cmd_2 = './hera/geom_bottleneck/build/bottleneck_dist ./persistence_diagrams/persistence_diagram_nonmetric_k_' + str(i+1) + '.txt ./persistence_diagrams/persistence_diagram_nonmetric_k_' + str(j+1) + '.txt >> bottleneck_values.txt'
        sp.call(['sh', '-c', cmd_1])
        sp.call(['sh', '-c', cmd_2])
        sp.call(['sh', '-c', cmd_3])