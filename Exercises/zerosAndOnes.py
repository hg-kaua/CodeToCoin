import numpy as np

# read the input values

shape = tuple(map(int, input().split()))

# create an array of the given shape filled with zeros

zero_arrays = np.zeros(shape, dtype=int)
 
# create an array of the given shape filled with ones

one_arrays = np.ones(shape, dtype=int)

print(zero_arrays)
print(one_arrays)