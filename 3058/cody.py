"""code"""
a = int(input())
b = int(input())
goal = int(input())

bigused = min(b,goal // 5)
remaining = goal - (bigused * 5)

if a >= remaining:
    print(remaining)
else:
    print(-1)
