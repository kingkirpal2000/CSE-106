import numpy as np

def create8by8():
    arr = np.zeros((8, 8))
    arr[0:8:2, 1:8:2] = 1
    arr[1:8:2, 0:8:2] = 1

    print(arr)


def create4by2():
    arr = np.arange(2, 10).reshape(4, 2)
    print(arr)

def uniqueVals():
    list = [10, 20,10,30, 20, 40, 20, 20, 10, 30, 0, 50, 10]
    arr = np.unique(list)
    print(arr)

def greaterthan37():
    list = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
    arr = np.array(list)
    arr = arr[arr>37]
    print(arr)

def CtoF():
    list = [0, 12, 45.21 ,34, 99.91]
    arr = np.array(list)
    arr = (arr*float(9/5)+32)
    print(arr)

def main():
    print("1a.")
    create4by2()
    print("\n")
    print("1b.")
    create8by8()
    print("\n")
    print("1c.")
    uniqueVals()
    print("\n")
    print("1d.")
    greaterthan37()
    print("\n")
    print("1e.")
    CtoF()
    print("\n")



if __name__ == "__main__":
    main()