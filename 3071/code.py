"""code"""
A = int(input())
B = int(input())
d = int(input())
r = int(input())
x = 0
for i in range(A,B+1):
    if i % d  == r:
        x += 1
print(x)
