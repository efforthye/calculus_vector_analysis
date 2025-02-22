# src/basic_linear_algebra/tensor_basics.py
import numpy as np

# 2x3 tensor 정의
tensor_x = np.array([[1, 2, 3], [2, 3, 4]])

# tensor 전체 출력
print(f"텐서: \n{tensor_x}")

# shape, rank(ndim) 확인
print(f"모양: {tensor_x.shape}")  # (2, 3)
print(f"차원: {tensor_x.ndim}")   # 2

# 행 개수 및 원소 확인
print(f"행 개수: {tensor_x.shape[0]}")  # 2
print(f"첫 원소: {tensor_x[0,0]}")      # 1

# 개별 원소 접근
print(f"(0,0) 위치 원소: {tensor_x[0,0]}")  # 1
print(f"(1,0) 위치 원소: {tensor_x[1,0]}")  # 2
print(f"(1,2) 위치 원소: {tensor_x[1,2]}")  # 4