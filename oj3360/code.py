"""code"""
w, h = map(int, input().split()[:2])
x = list(map(int, input().split()))
y = list(map(int, input().split()))

edge_x = [0] + x + [w]
gap_x = [b - a for a, b in zip(edge_x, edge_x[1:])]
W = sorted(gap_x, reverse=True)

edge_y = [0] + y + [h]
gap_y = [b - a for a, b in zip(edge_y, edge_y[1:])]
H = sorted(gap_y, reverse=True)

cand = [W[0] * H[0]]
if len(W) > 1:
    cand.append(W[1] * H[0])
if len(H) > 1:
    cand.append(W[0] * H[1])
cand.sort(reverse=True)

print(cand[0], cand[1] if len(cand) > 1 else cand[0])
