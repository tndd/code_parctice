from collections import Counter

N = int(input())
S = list(input())

sc = Counter(S)

cnt = 1
for char, n in sc.items():
    cnt *= (n + 1)

print((cnt - 1) % (10**9 + 7))
