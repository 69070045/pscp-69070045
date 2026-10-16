"""c0de"""
import math as m
name = input().split()
l = int(name[0])
n = int(name[1])
nub = 1
step = 0
tab = 1

while nub <= n:
    nub += tab
    tab += 1
    step += 1
print(m.ceil(step / l))
