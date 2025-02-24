# python src/basic_linear_algebra/matrix/matrix_2x3.py
import numpy as np

# 2x3 matrix 정의
matrix_x = np.array([[1, 2, 3], [2, 3, 4]])

# matrix 전체 출력
print(f"행렬: \n{matrix_x}")

# shape, rank(ndim) 확인
print(f"모양: {matrix_x.shape}")  # (2, 3)
print(f"차원: {matrix_x.ndim}")   # 2

# 행 개수 및 원소 확인
print(f"행 개수: {matrix_x.shape[0]}")  # 2
print(f"첫 원소: {matrix_x[0,0]}")      # 1

# 개별 원소 접근
print(f"(0,0) 위치 원소: {matrix_x[0,0]}")  # 1
print(f"(1,0) 위치 원소: {matrix_x[1,0]}")  # 2
print(f"(1,2) 위치 원소: {matrix_x[1,2]}")  # 4