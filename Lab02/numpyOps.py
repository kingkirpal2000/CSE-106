import numpy as np
from numpy import linalg

def AplusB(A, B):
    print(A+B)
def AmultB(A, B):
    print(A*B)
def Det(A):
    print(linalg.det(A))
def Inv(A):
    print(linalg.inv(A))
def Eig(A):
    print(linalg.eigvals(A))

def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    B = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])
    print("MATRIX A\n")
    print(A)
    print("MATRIX B\n")
    print(B)
    print("2a.\n")
    AplusB(A, B)
    print("2b.\n")
    AmultB(A, B)
    print("2c.\n")
    Det(A)
    print("2d.\n")
    Inv(B)
    print("2e.\n")
    Eig(A)



if __name__ == "__main__":
    main()