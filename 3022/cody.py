"""code"""
temp = float(input())
unit1 = input()
unit2 = input()
unitC = 0

if unit1 == "C":
    unitC = temp
elif unit1 == "F":
    unitC = ((temp - 32) * 5) / 9
elif unit1 == "K":
    unitC = temp - 273.15
elif unit1 == "R":
    unitC = ((temp * 5) / 9) - 273.15

if unit2 == "C":
    print(f"{unitC:.2f}")
elif unit2 == "F":
    print(F"{((unitC * 9) / 5) + 32:.2f}")
elif unit2 == "K":
    print(f"{unitC + 273.15:.2f}")
elif unit2 == "R":
    print(f"{((unitC + 273.15) * 9) / 5:.2f}")
