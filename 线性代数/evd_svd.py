import numpy as np

# EVD
A = np.array([[1, 2, 2],
             [2, 1, 2],
             [2, 2, 1]])

# sovle A's eigenvalues and eigenvectors
evalues,evectors = np.linalg.eig(A)
# print(evalues[0] * evectors[:,0])
# print(A @ evectors[:,0]) #列向量为其特征向量
# print(np.sum(evectors[:,0]*evectors[:,0])) #1,已经标准化

# valid A = W @ sigma @ W.T , W = e
W = evectors
sigma =  np.zeros_like(evectors)
for i in range(len(evalues)):
    sigma[i,i] = evalues[i]

# print(A)
# print(W @ sigma @ W.T)

# SVD
B = np.array([[1, 2],
             [2, 1],
             [2, 2]])
U,sigma,V = np.linalg.svd(B)
print("U",U)
print("sigma",sigma)
print("V",V)

_,U2 = np.linalg.eig(B@B.T)
_,V2 = np.linalg.eig(B.T@B)
sigma2 = np.zeros_like(B,dtype=np.float64)
for i in range(min(B.shape)):
    print(V2[:,i])
    print(B@V2[:,i])
    print(U2[:,i])
    print(B@V2[:,i]/U2[:,i]) #有误差,因为被除数可能很小
    print("-"*30)
    r = B@V2[:,i]/U2[:,i]
    argmin = np.argmin(np.abs(r)) #选个绝对值最小的，照道理是完全一样的
    sigma2[i,i] = r[argmin]
print(sigma2)

# valid B = U2 @ sigma2 @ V2.T
print(B)
print(U2 @ sigma2 @ V2.T)
