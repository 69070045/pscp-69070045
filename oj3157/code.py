"""c0de"""
num = int(input())
score = 0

for i in range(num):
    i = input()
    if i == "+":
        score += 10
    elif i == "-":
        score -= 5

print(score)
