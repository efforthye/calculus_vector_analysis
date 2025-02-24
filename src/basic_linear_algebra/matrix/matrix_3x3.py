# python src/basic_linear_algebra/matrix/matrix_3x3.py
import numpy as np

# 3x3 matrix 정의
matrix_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# matrix 전체 출력
print(f"텐서: \n{matrix_a}")

# shape, rank(ndim) 확인
print(f"모양: {matrix_a.shape}")  # (3, 3)
print(f"차원: {matrix_a.ndim}")   # 2

# 행 개수 및 원소 확인
print(f"행 개수: {matrix_a.shape[0]}")  # 3
print(f"첫 원소: {matrix_a[0,0]}")      # 1

# 개별 원소 접근
print(f"(0,0) 위치 원소: {matrix_a[0,0]}")  # 1
print(f"(0,1) 위치 원소: {matrix_a[0,1]}")  # 2
print(f"(2,1) 위치 원소: {matrix_a[2,1]}")  # 8