"""code"""
months = int(input())
day = int(input())
if months in (1,2):
    print("winter")
elif months == 3 and day < 21:
    print("winter")
elif months == 3 and day >= 21:
    print("spring")
elif months in (4,5):
    print("spring")
elif months == 6 and day < 21:
    print("spring")
elif months == 6 and day >= 21:
    print("summer")
elif months in (7,8):
    print("summer")
elif months == 9 and day < 21:
    print("summer")
elif months == 9 and day >= 21:
    print("fall")
elif months in (10,11):
    print("fall")
elif months == 12 and day < 21:
    print("fall")
elif months == 12 and day >= 21:
    print("winter")
