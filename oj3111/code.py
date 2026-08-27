"""SahakornSchool"""
name = input()
raka = int(input())
price = []
for _ in range(raka):
    price.append(float(input()))
total = sum(price)
finaltotal = total
if name == "Y":
    discount = total * 0.05
    finaltotal = total - discount
elif name == "N":
    if total >= 500:
        discount = total * 0.03
        finaltotal = total - discount
    else:
        finaltotal = total
    #เพิ่ม 0.000000001 เพื่อแก้ปัญหาความคลาดเคลื่อนของ float
fixtotal = round(finaltotal + 1e-9,2)
print(f"{fixtotal:.2f}")
