"""Code"""
n, s = map(int, input().split())
PASS = [0] * (n + 1)

for i in range(1, n + 1):
    PASS[i] = int(input())

view = set()
cur = s

while cur and cur not in view:
    view.add(cur)
    cur = PASS[cur]

print(len(view))
