""" Practice Exercises for Midterm Exam """

import numpy as np

a = np.array([[0, 1, 2, 3], [4,5,6,7], [8, 9, 10, 11]])
i = np.array([[0, 1], [1, 2]])
j = np.array([[2, 3], [1, 0]])

print a
print i
print j

print a[i, j]