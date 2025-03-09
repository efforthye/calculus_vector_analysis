# python src/basic_linear_algebra/matrix/equal_matrices.py
import numpy as np

A = np.random.randint(2, size=(2,3))
B = np.random.randint(2, size=(2,3))
print("A=", A, "\n")
print("B=", B, "\n")

flag = True

for i in range(2):
    for ii in range(3):
        if(A[i, ii] != B[i, ii]):
            print(f"(A[{i}, {ii}] = {A[i, ii]}) != (B[{i}, {ii}] = {B[i, ii]})\n")
            flag = False
            break
    if(flag == False):
        break

if(flag):
    print("[flag] Matrices A and B are equal")
else:
    print("[flag] Thus, matrices A and B are not equal")
if np.array_equal(A, B):
    print("[array_equal] Matrices A and B are equal")
else:
    print("[array_equal] Thus, matrices A and B are not equal")
