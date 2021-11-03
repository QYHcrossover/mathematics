import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 4, 9],
                 [2, 5, 8],
                 [3, 6, 9]])
    det = np.linalg.det(A)
    print("A的行列式为:",det) #-6

    inv = np.linalg.inv(A)
    print("A的逆矩阵:\n {}".format(inv))

    rank = np.linalg.matrix_rank(A)
    print("A的秩",rank)

    B = np.array([[1, 2, 9],
                [2, 4, 8],
                 [3, 6, 9]])
    det = np.linalg.det(B)
    print("B的行列式为:",det) #0

    inv = np.linalg.inv(B)
    print("B的逆矩阵:\n {}".format(inv)) #报错

    rank = np.linalg.matrix_rank(B) #2
    print("B的秩",rank)



