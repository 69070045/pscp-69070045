"""code"""
def main():
    """code"""
    n, k, t = map(int, input().split())

    if t == 1:
        print(1)
        return
    yunaii = 1
    nub = 1

    while True:
        konenn = (yunaii - 1 + k) % n + 1
        if konenn == 1:
            break
        if konenn == t:
            nub += 1
            break
        nub += 1
        yunaii = konenn
    print(nub)
main()
