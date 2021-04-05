from math import gcd
from functools import reduce

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

a_mx = max(A)
gcd = reduce(gcd, A)
if a_mx >= K and (a_mx - K) % gcd == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
