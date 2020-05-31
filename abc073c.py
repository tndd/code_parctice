from collections import Counter
N = int(input())
a_counter = Counter([int(input()) for _ in range(N)])

ans = 0
for num, cnt in a_counter.items():
  if cnt % 2 == 1:
    ans += 1

print(ans)