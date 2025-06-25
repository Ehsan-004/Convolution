from pprint import pprint
import time
import os


def Conv1D(data: list, kernel: list, stride: int = 1):
    if len(kernel) > len(data):
        raise ValueError("len(kernel) is larger than len(data)")
    
    if len(data) == 0 or len(kernel) == 0:
        raise ValueError("kernel or data has length of 0 !")
    
    if stride < 1: 
        raise ValueError("stride must be non-zero and pozitive")
    
    kernel_len = len(kernel)
    max_index = len(data) - kernel_len + 1
    for i in range(0, max_index, stride):
        if i > len(data):
            break
        for j in range(kernel_len):
            data[i+j] *= kernel[j]
    return data


if __name__ == "__main__":
    kernel = [2,2,2]
    for i in range(1, 15):
        m = [1 for _ in range(10)]
        pprint(Conv1D(m, kernel, i))
