from pprint import pprint
import time
import os


l = 10
m = ["#" for _ in range(l)]

print(m)
time.sleep(2)


kernel_len = 3
start_index = 0

max_index = len(m) - kernel_len + 1


for i in range(max_index):
    # os.system("cls")
    m = ["#" for _ in range(l)]
    # m[i: kernel_len] = ["*" for _ in range(kernel_len)]
    for j in range(i, i+ kernel_len):
        m[j] = "0"
    pprint(m)
    time.sleep(1)
