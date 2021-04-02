from collections import Counter
from math import factorial

N = int(input())
T = [int(input()) for _ in range(N)]

T.sort()
tc = Counter(T)

pn = 1
for t, n in tc.items():
    pn *= factorial(n)

time = 0
cost = 0
for n in T:
    cost += time + n
    time += n

print(cost)
print(pn % (10**9 + 7))
