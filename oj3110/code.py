""""code"""
express1,express2 = input().upper().split()
kg = float(input())
if express1 == "BKK" and express2 == "CNX":
    print(f"{10 + (kg * 30):.2f}")
elif express1 == "CNX" and express2 == "UBP":
    print(f"{15 + (kg * 40):.2f}")
elif express1 == "UBP" and express2 == "BKK":
    print(f"{20 + (kg * 40):.2f}")
elif express1 == "BKK" and express2 == "PKT":
    print(f"{25 + (kg * 50):.2f}")
elif express1 == "PKT" and express2 == "CNX":
    print(f"{30 + (kg * 60):.2f}")
elif express1 == "UBP" and express2 == "PKT":
    print(f"{40 + (kg * 70):.2f}")
else:
    print("Error")
