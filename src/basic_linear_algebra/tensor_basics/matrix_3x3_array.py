# python src/basic_linear_algebra/tensor_basics/matrix_3x3_array.py
import numpy as np

# 3차원 텐서 정의 (2개의 3x3 matrix)
matrix_a = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 
                    [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

# matrix 전체 출력
print(f"텐서: \n{matrix_a}")

# shape, rank(ndim) 확인
print(f"모양: {matrix_a.shape}")  # (2, 3, 3)
print(f"차원: {matrix_a.ndim}")   # 3

# 첫 번째 차원 개수 및 첫 번째 행렬의 첫 원소 확인
print(f"행렬 개수: {matrix_a.shape[0]}")   # 2
print(f"첫 원소: {matrix_a[0,0,0]}")      # 1

# 개별 원소 접근
print(f"(0,0,0) 위치 원소: {matrix_a[0,0,0]}")  # 1
print(f"(0,0,1) 위치 원소: {matrix_a[0,0,1]}")  # 2
print(f"(0,2,1) 위치 원소: {matrix_a[0,2,1]}")  # 8
print(f"(1,0,0) 위치 원소: {matrix_a[1,0,0]}")  # 10