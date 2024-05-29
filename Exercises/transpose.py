import numpy as np


n, m = map(int, input().split())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

np_matrix = np.array(matrix)
transpose_matrix = np_matrix.T
flattened_matrix = np_matrix.flatten()
print(transpose_matrix)
print(flattened_matrix)
