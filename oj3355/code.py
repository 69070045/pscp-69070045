"""code"""
n = []
while True:
    i = int(input())
    if i == -1:
        break
    n.append(i)

lists = []
if n:
    start = I = n[0]
    for i in n[1:]:
        if i == I + 1:
            I = i
            continue

        if start == I:
            lists.append(str(start))
        else:
            lists.append(f"{start}-{I}")

        start = I = i

    if start == I:
        lists.append(str(start))
    else:
        lists.append(f"{start}-{I}")

    print(", ".join(lists))
