"""code"""
T = int(input())

for _ in range(T):
    n = int(input())
    list_P = []
    for _ in range(n):
        x, y = map(int, input().split())
        list_P.append((x, y))
    list_P.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in list_P:
        print(x, y)
