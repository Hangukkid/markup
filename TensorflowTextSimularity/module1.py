
import numpy as np
import os
import io

d = open('data.txt')
dStr = d.read()
dIO = io.StringIO(dStr)
Dat = np.loadtxt(dIO, dtype=str, delimiter="\t", usecols = (0, 1))

l = open('label.txt')
lStr = l.read()
lIO = io.StringIO(lStr)
Lab = np.loadtxt(lIO, dtype=int, delimiter="\t")

print(Dat)
print(Lab)