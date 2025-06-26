from pprint import pprint
import time
import os
from math import floor


def Conv2D(data: list[list], kernel: list[list], stride: int = 1, padding: int = 0, fill: int = 0):
    
    # kernel = [[2 for __ in range(kr)] for _ in range(kl)]
    # data = [[1 for __ in range(r)] for _ in range(l)]
    
    l = len(data)
    r = len(data[0])
    kl = len(kernel)
    kr = len(kernel[0])
    
    feature_map_l = floor((l - kl + 2 * padding) / stride) + 1
    feature_map_r = floor((l - kr + 2 * padding) / stride) + 1
            
    max_line = l - kl + 1
    max_row = r - kr + 1
    
    feature_map = [[[] for __ in range(max_row)] for _ in range(max_line)]
    
    for i in range(0, max_line):  # i corresponds to line
        for j in range(max_row):  # j corresponds to row
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
    pprint(m)
    time.sleep(1)
    os.system("cls")
    pprint(Conv2D(m, kernel))
