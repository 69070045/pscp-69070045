"""code"""
text = [input() for _ in range(5)]
raya = max(len(t) for t in text)
print("*" * (raya + 4))

for _ in text:
    print(f"* {_:<{raya}} *")

print("*" * (raya + 4))
