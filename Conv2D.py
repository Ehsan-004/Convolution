from pprint import pprint
import time
import os

l = 9
r = 9

kl = 3
kr = 3

def Conv2D(data: list[list], kernel: list[list]):
    
    kernel = [["-" for __ in range(kr)] for _ in range(kl)]
    data = [["-" for __ in range(r)] for _ in range(l)]
            
    max_line = len(data) - len(kernel) + 1
    max_row = len(data[0]) - len(kernel[0]) + 1
    
    # pprint(data)
    
    for i in range(0, max_line):  # i corresponds to line
        for j in range(max_row):  # j corresponds to row
            data = [["-" for __ in range(r)] for _ in range(l)]
            for m in range(kl):
                for n in range(kr):
                    data[i+m][j+n] = "0"
            
            pprint(data)
            time.sleep(0.25)
            os.system("cls")
    return data


if __name__ == "__main__":
    kernel = [2,2,2]
    
    m = [1 for _ in range(10)]
    Conv2D(m, kernel)
