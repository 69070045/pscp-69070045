"""Code"""
n = int(input())
h = []

for _ in range(n):
    h.append(int(input()))

count = 0

for i in range(n):
    L = not i or h[i] > h[i - 1]
    R = i == n - 1 or h[i] > h[i + 1]
    if L and R:
        count += 1

print(count)
