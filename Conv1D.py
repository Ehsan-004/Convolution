from pprint import pprint
import time
import os


def Conv1D(data: list, kernel: list):
    kernel_len = len(kernel)
    max_index = len(data) - kernel_len + 1
    for i in range(max_index):
        for j in range(kernel_len):
            data[i+j] *= kernel[j]
    return data


if __name__ == "__main__":
    kernel = [2,2,2]
    m = [1 for _ in range(10)]
    pprint(Conv1D(m, kernel))
