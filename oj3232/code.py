"""code"""
num = input().split()
x = int(num[0])
y = int(num[1])
raya = 0
nubjump = 0
rayajump = x

while raya < y:
    if rayajump <= 0:
        nubjump = -1
        break
    raya += rayajump
    nubjump += 1
    rayajump -= 2

print(nubjump)
