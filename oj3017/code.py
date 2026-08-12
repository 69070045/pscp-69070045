"""code"""
discount = int(input())
service = discount * 0.1
servicecharge = int()
if service <= 50:
    servicecharge = 50
elif service >= 1000:
    servicecharge = 1000
else:
    servicecharge = service
VAT = (discount + servicecharge) * 0.07
Total = discount + VAT + servicecharge
print(f"{Total:.2f}")
