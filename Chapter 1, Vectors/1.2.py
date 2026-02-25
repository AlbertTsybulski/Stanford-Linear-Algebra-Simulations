import numpy as np

"""
Section a
"""
x = np.random.random(10) #A random 10-vector
a = np.eye(10)[4] #A unit vector with a 1 in the 5th position

print("(a) ", np.dot(a, x)) #The inner product of a and x is the 5th element of x

"""
Section b
"""
x = np.random.random(3) #A random 3-vector
a = np.array([0.3, 0.4, 0.3]) #A vector giving the weights for a weighted average

print("(b) ", np.dot(a, x)) #The inner product of a and x is the weighted average of the elements of x

"""
Section c
"""
x = np.random.random(22) #A random 22-vector
multfour = np.array([1 if i % 4 == 0 else 0 for i in range(22)]) #A vector with 1s in the positions that are multiples of 4
multseven = np.array([1 if i % 7 == 0 else 0 for i in range(22)]) #A vector with 1s in the positions that are multiples of 7

print("(c) ", np.dot(multfour, x) - np.dot(multseven, x)) #The inner product of multfour and x minus the inner product of multseven and x is the sum of the elements of x in the positions that are multiples of 4 minus the sum of the elements of x in the positions that are multiples of 7

"""
Section d
"""
x = np.random.random(11) #A random 11-vector
a = np.array([0.2 if 3<=i<=7 else 0 for i in range(11)]) #A vector with 0.2s in the middle 5 entries and 0s elsewhere

print("(d) ", np.dot(a, x)) #The inner product of a and x is the average of the elements of x in the middle 5 entries