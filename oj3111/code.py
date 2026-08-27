"""code"""
name = input()
raka = int(input())
price = []

for _ in range(raka):
    price.append(float(input()))
sumprice = sum(price)
allsum = sumprice

if name == "Y":
    discount = sumprice * 0.05
    allsum = sumprice - discount
elif name == "N":
    if sumprice >= 500:
        discount = sumprice * 0.03
        allsum = sumprice - discount
    else:
        allsum = sumprice

a = round(allsum + 1e-9,2)
print(f"{a:.2f}")
