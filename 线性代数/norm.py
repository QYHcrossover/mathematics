import numpy as np

# 向量的范数
a = np.arange(6)
print(np.linalg.norm(a,ord=1))
print(np.linalg.norm(a,ord=2))
print(np.linalg.norm(a,ord=np.inf))

# 矩阵的范数
A = np.arange(12).reshape((3,4))
print(A)
print(np.linalg.norm(A,ord=1))
print(np.linalg.norm(A,ord=2))
print(np.linalg.norm(A,ord=np.inf))
print(np.linalg.norm(A,ord="fro"))

print(np.linalg.norm(A,ord=2,axis=0)) #列向量的2范数
print(np.linalg.norm(A,ord=2,axis=1)) #行向量的2范数