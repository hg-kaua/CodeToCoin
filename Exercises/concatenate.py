
import numpy as np

# read the input values

n, m, p = map(int, input().split())

# read the first array

array1 = []

for _ in range(n):
    row = list(map(int, input().split()))
    array1.append(row)
    
# read the second array

array2 = []

for _ in range(m):
    row = list(map(int, input().split()))
    array2.append(row)
    
    
# convert list to numpy arrays

array1 = np.array(array1)
array2 = np.array(array2)

# concatenate the array along axis 0 rows

result = np.concatenate((array1, array2), axis=0)

print(result)