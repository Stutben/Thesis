import os
import csv

import numpy as np
import matplotlib.pyplot as plt


metric = 'tuple_latency'

alg = 'Alg1'

directory = 'C:\\Users\\Beni\\CEP\\'+ alg +'\\'
directories = next(os.walk(directory))[1]

paths = list()

for folder in directories:
    paths.append(directory + folder + '\\Topology_FileReadSpout.log')

x = list()
y = list()
for file in paths:

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            x.append(row['minutes_since_start'])
            y.append(row[metric])

x = [int(i) for i in x]
y = [float(i) for i in y]

fn = np.poly1d(np.polyfit(x, y, 4))
x_new = np.linspace(x[0], x[-1])


######################################################################
######################Do same for other algo##########################
######################################################################

alg = 'Alg2'

directory = 'C:\\Users\\Beni\\CEP\\'+ alg +'\\'
directories = next(os.walk(directory))[1]

paths = list()

for folder in directories:
    paths.append(directory + folder + '\\Topology_FileReadSpout.log')

x2 = list()
y2 = list()
for file in paths:

    with open(file) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            x2.append(row['minutes_since_start'])
            y2.append(row[metric])

x2 = [int(i) for i in x2]
y2 = [float(i) for i in y2]

fn2 = np.poly1d(np.polyfit(x2, y2, 4))
x2_new = np.linspace(x2[0], x2[-1])


##################create two diagrams##########
fig, ax = plt.subplots(1, 2)

###################Set label###################
ax[0].set_xlabel('minutes_since_start')
ax[0].set_ylabel(metric+ " in ms")
ax[1].set_xlabel('minutes_since_start')
ax[1].set_ylabel(metric + " in ms")

###################Title###################
ax[0].set_title("Warteschlangen-Theorie")
ax[1].set_title("Regression")

#################Limits###############
ax[0].set_ylim(0, 20000)
ax[1].set_ylim(0, 20000)

ax[0].grid(True, 'both', 'both')
ax[1].grid(True, 'both', 'both')

###################Plot########################
ax[0].plot(x, y, 'k+', x_new, fn(x_new), 'r')
ax[1].plot(x2, y2, 'k+', x2_new, fn2(x2_new), 'r')
plt.show()