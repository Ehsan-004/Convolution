from pprint import pprint
import time
import os


l = 10
m = [1 for _ in range(l)]

print(m)
time.sleep(2)


kernel_len = 3
kernel = [2,2,2]
start_index = 0

max_index = len(m) - kernel_len + 1


for i in range(max_index):
    # os.system("cls")
    # m = [1 for _ in range(l)]
    
    for j in range(kernel_len):
        m[i+j] *= kernel[j]
    pprint(m)
    time.sleep(1)

print(m)


def Conv1D(data: list, kernel: list):
    pass
