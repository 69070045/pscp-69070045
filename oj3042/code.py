"""c0de"""
num = int(input())
X = num - (num % 10)
A = []
for i in range(X,-1,-10):
    i -= 0
    A.append(str(i))
print(" ".join(A))
