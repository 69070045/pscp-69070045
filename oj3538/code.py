"""code"""
pair = input()
not_pair = ""
check = []

for i in pair:
    if i not in check:
        check.append(i)
        count = pair.count(i)
        if count % 2:
            not_pair += i

if not not_pair:
    print("fully paired")
else:
    print(not_pair)
