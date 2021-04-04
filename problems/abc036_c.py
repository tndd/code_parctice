N = int(input())
a = [int(input()) for _ in range(N)]

d = {}
for i, n in enumerate(sorted(set(a))):
    d[n] = i

for n in a:
    print(d[n])
