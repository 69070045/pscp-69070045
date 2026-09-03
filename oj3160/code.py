"""code"""
n1, n2 = input().split()
n1 = int(n1)
n2 = int(n2)
jumnon_prime = 0
primes_tua = []

for N in range(n1, n2 + 1):
    if N <= 1:
        continue
    prime = True
    for i in range(2, N):
        if not N % i:
            prime = False
            break
    if prime:
        primes_tua.append(N)
        jumnon_prime += 1

if primes_tua:
    print(*primes_tua)
    print(f"Total primes: {jumnon_prime}")
else:
    print(f"Total primes: {jumnon_prime}")
