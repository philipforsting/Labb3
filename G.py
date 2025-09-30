import matplotlib.pyplot as plt # For plotting grafs
import numpy as np              # For array manipulation
import pandas as pd             # For storing array as .csv-file

def ClassifyPoints(points, k, m):
    """The function will classify the points an np-array, checking if the points are above/rigt of a line specified as k*x+m. Classification added in added third row"""
    pointsZeroColumn = np.zeros((points.shape[0], 1))           # Prepairing to store classification result in points array
    points = np.column_stack((points, pointsZeroColumn)) 
    for point in points:
        point[2] = bool(point[1] > k*point[0] + m)
    return points

# MAIN
def main():
    k = -1
    m = 0

    unlabelled_data = np.genfromtxt("unlabelled_data.csv", delimiter=",")
    labelled_data = ClassifyPoints(unlabelled_data, k=k, m=m)
    labelled_data_fd = pd.DataFrame(labelled_data)
    labelled_data_fd.to_csv("labelled_data.csv")

    labelled_data_0 = labelled_data[labelled_data[:,2] == 0]        # Exratracting rows from np array with mask. Inspiration taken from https://stackoverflow.com/questions/58079075/numpy-select-rows-based-on-condition
    labelled_data_1 = labelled_data[labelled_data[:,2] == 1]       
    line_x = np.array([-5,5])                                       

    plt.axis([-5,5,-5,5])                                           # Locking axis
    plt.scatter(labelled_data_0[:,0], labelled_data_0[:,1])
    plt.scatter(labelled_data_1[:,0], labelled_data_1[:,1])
    plt.plot(line_x, -line_x, color = 'r')
    plt.legend(("Points below (left hand side of) line", "Points above (right hand side of) line", "y(x) = -x"))
    plt.show()

if __name__ == "__main__":   # The following rows have been copied from https://realpython.com/python-main-function/
    main()