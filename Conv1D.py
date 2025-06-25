from pprint import pprint
import time
import os
from math import ceil


def Conv1D(data: list, kernel: list, stride: int = 1, padding: int = 0, fill: int = 0):
    if len(kernel) > len(data):
        raise ValueError("len(kernel) is larger than len(data)")
    
    if len(data) == 0 or len(kernel) == 0:
        raise ValueError("kernel or data has length of 0 !")
    
    if stride < 1: 
        raise ValueError("stride must be non-zero and pozitive")
    
    data = [fill for i in range(padding)] + data + [fill for i in range(padding)]
    kernel_len = len(kernel)
    
    feature_map = []
       
    max_index = len(data) - kernel_len + 1
    for i in range(0, max_index, stride):
        sum_ = 0
        if i > len(data):
            break
        for j in range(kernel_len):
            tmp = data[i+j] * kernel[j]
            data[i+j] = tmp
            sum_ += tmp
        feature_map.append(sum_)
    return data, feature_map


if __name__ == "__main__":
    m = [2, 3, 4, 5, 1, 2]
    kernel = [2,2]
    
    res = Conv1D(m, kernel, 2)
    feature_map_len = ceil((len(m) - (len(kernel) - 1)) / (1))
    print(feature_map_len)
    pprint(res[0])
    print(res[1])
