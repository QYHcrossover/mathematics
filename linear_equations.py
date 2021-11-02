import numpy as np

if __name__ == "__main__":
    A = [[4,6,2],
         [3,4,1],
         [2,8,13]]
    s = [9,7,2]
    r = np.linalg.solve(A,s)
    print(r)