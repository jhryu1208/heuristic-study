import numpy as np

def count_one(object: np.array)->int:
    return object.sum()

if __name__ == '__main__':
    x = np.array([1,0,1,1])
    print(count_one(x))