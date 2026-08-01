"""code"""
overallpoint = float(input())
maxpoint = float(input())
minpoint = overallpoint - (maxpoint * 2)
if minpoint < 0:
    minpoint = 0

if maxpoint - minpoint > 2:
    print("Surprising")
else:
    print("Not surprising")
