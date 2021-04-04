N = int(input())
a = [int(input()) for _ in range(N)]

_a = list(set(sorted(a)))
for n in a:
    print(_a.index(n))
