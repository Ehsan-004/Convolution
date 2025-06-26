from pprint import pprint
import time
import os
from math import floor


def Conv2D(data: list[list], kernel: list[list], stride: int = 1, padding: int = 0, fill: int = 0):
    
    l = len(data)
    r = len(data[0])
    kl = len(kernel)
    kr = len(kernel[0])
    
    if padding < 0:
        raise ValueError(f"padding cannot be smaller than 0 but got {padding}")
    elif padding > 0:
        for i in range(0, l):
            for _ in range(padding):
                data[i].append(fill)
        
        for _ in range(padding):
            data.append([fill for __ in range(r + padding)])
        
    l = len(data)
    r = len(data[0])
    
    
    lines = floor((l - kl + 2 * padding) / stride) + 1
    rows = floor((r - kr + 2 * padding) / stride) + 1
    
    feature_map = [[[] for __ in range(rows)] for _ in range(lines)]
        
    for i in range(0, lines):  # i corresponds to line
        for j in range(0, rows):  # j corresponds to row
            sum_ = 0
            for m in range(kl):
                for n in range(kr):
                    tmp = data[i+m][j+n] * kernel[m][n]
                    data[i+m][j+n] = tmp
                    sum_ += tmp
            feature_map[i][j] = sum_
                    
    return data, feature_map


if __name__ == "__main__":
    kernel = [[2,2],
              [2,2]]
    
    m = [[1,1,1,1],
         [2,2,2,2],
         [1,1,1,1],
         ]
    os.system("cls")
    pprint(m)
    time.sleep(1)
    os.system("cls")
    r = Conv2D(m, kernel, 2, padding=2, fill=0)
    
    pprint(r[0])
    pprint(r[1])
