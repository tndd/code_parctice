import math

N, H = list(map(int, input().split()))
a = []
b = []
for i in range(N):
    _a, _b = list(map(int, input().split()))
    a.append(_a)
    b.append(_b)

a_mx = max(a)
b.sort(reverse=True)
turn = 0
while H > 0:
    if len(b) > 0 and a_mx < b[0]:
        H -= b.pop(0)
        turn += 1
    else:
        turn += int(math.ceil(H / a_mx))
        H = 0

print(turn)
