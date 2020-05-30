n = int(input())
a = list(map(int, input().split()))
b = []

for i in range(n):
  b.append(a.pop(0))
  b = b[::-1]

print(' '.join(map(str, b)))