from pprint import pprint
import time
import os
from math import floor
import copy


def Pooling(data: list[list], kernel_size: tuple[int, int], stride: int = 1, padding: int = 0, fill: int = 0, method="max"):
    # methodes: ["max", "min", "avg"]
    
    original_l = len(data)
    original_r = len(data[0])
    
    kl, kr = kernel_size
    
    # adding padding if padding
    if padding < 0:
        raise ValueError(f"padding cannot be smaller than 0 but got {padding}")
    elif padding > 0:
        
        padded_l = original_l + 2 * padding
        padded_r = original_r + 2 * padding
        
        for li in data:
            p = [padding * fill for _ in range(padding)]
            for f in reversed(p):
                li.insert(0, f)
            for f in p:
                li.append(f)

            
        for _ in range(padding):
            data.insert(0, [fill for _ in range(padded_r)])
            data.append([fill for _ in range(padded_r)])
        
    orig_l = len(data)
    orig_r = len(data[0])
    
    fmap_lines = floor((original_l - kl + 2 * padding) / stride) + 1
    fmap_rows = floor((original_r - kr + 2 * padding) / stride) + 1
    
    feature_map = [[0 for __ in range(fmap_rows)] for _ in range(fmap_lines)]
        
        
    # print("orig_l - kl + 1 = ", orig_l - kl + 1)
    # print("original_r - kr + 1 = ", )
    for i in range(0, orig_l - kl + 1, stride):  # i corresponds to line
        for j in range(0, orig_r - kr + 1, stride):  # j corresponds to row
            pv = []
            for m in range(kl):
                for n in range(kr):
                    pv.append(data[i+m][j+n])
            # uncomment this part to see what happens!
            # pprint(data_c)
            # time.sleep(1)
            # os.system("cls")
            
            if method == "max":
                feature_map[i//stride][j//stride] = max(pv)
            elif method == "min":
                feature_map[i//stride][j//stride] = min(pv)
            elif method == "avg":
                feature_map[i//stride][j//stride] = sum(pv) / len(pv)
                
    return feature_map



def MaxPool2D(data: list[list], kernel_size: tuple[int, int], stride: int = 1, padding: int = 0, fill: int = 0):
    return Pooling(data, kernel_size, stride , padding, fill, method="max")


def MinPool2D(data: list[list], kernel_size: tuple[int, int], stride: int = 1, padding: int = 0, fill: int = 0):
    return Pooling(data, kernel_size, stride , padding, fill, method="min")


def AvgPool2D(data: list[list], kernel_size: tuple[int, int], stride: int = 1, padding: int = 0, fill: int = 0):
    return Pooling(data, kernel_size, stride , padding, fill, method="avg")



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
    # r = Conv2D(m, kernel, 2, padding=2, fill=0)
    r = MaxPool2D(m, kernel, 1, padding=2, fill=0)
    
    pprint(r)
    # pprint(r[1])
