#Labb 3 förberedelser


import matplotlib.pyplot as plt
import numpy as np

unlabelled_data = np.genfromtxt("unlabelled_data.csv", delimiter=",")
print(unlabelled_data)
plt.scatter(unlabelled_data[:,0], unlabelled_data[:,1])

line_x = np.array([-5,5])

plt.plot(line_x, -line_x)
plt.show()