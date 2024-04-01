# readlines.py
import numpy as np
f = open("basics.txt", 'r')
arr = []
for line in f:
    line = line.strip()
    list= line.split('	', 6)
    arr.extend([list])
    gwamok = np.array(arr)
f.close()
