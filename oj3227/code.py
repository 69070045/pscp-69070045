"""code"""
pai = input().upper()
tam = pai[:-1]
dot = pai[-1]

dicttam = {"A": "ace", "J": "jack", "Q": "queen", "K": "king"}
dicdot = {"D": "diamonds", "H": "hearts", "S": "spades", "C": "clubs"}

num = dicttam.get(tam, tam)
print(f"{num} of {dicdot[dot]}")
