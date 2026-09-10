"""code"""
you = input().split()
me = input().split()
A = you[0]
B = you[1]
a = me[0]
b = me[1]

if A == a and B == b:
    print("1000000")
elif A != a and B == b:
    print("100000")
elif A == a and B[-3:] == b[-3:]:
    print("2000")
elif A == a and B[-2:] == b[-2:]:
    print("1000")
elif A != a and B[-3:] == b[-3:]:
    print("200")
elif A != a and B[-2:] == b[-2:]:
    print("100")
elif A == a and B != b:
    print("20")
else:
    print("0")
