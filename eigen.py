import numpy as np

if __name__ == "__main__":
    A = np.array([[1, 4, 9],
                 [2, 5, 8],
                 [3, 6, 9]])
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print(eigenvalues)
    print(eigenvectors)