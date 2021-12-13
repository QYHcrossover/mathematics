import numpy as np

if __name__ == "__main__":
    #构造一组线性无关的向量组，排列出矩阵
    A = np.array([[0,1,1],
                [1,0,1],
                [1,1,0]],dtype=np.float64)

    #正交化
    B = A.copy()
    for i in range(len(A)):
        for j in range(i):
            B[:,i] -= (A[:,i]*B[:,j]).sum() / (B[:,j]*B[:,j]).sum() * B[:,j]
    print(B)

    #标准化
    for i in range(len(B)):
        B[:,i] = B[:,i] / np.linalg.norm(B[:,i])
    print(B)

    #验证结果，结果应该是一个E单位矩阵
    print(B @ B.T)