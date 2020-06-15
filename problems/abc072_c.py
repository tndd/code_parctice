from collections import Counter

N = int(input())
A = list(map(int, input().split()))

a_all = []
for a in A:
  a_all.append(a)
  a_all.append(a - 1)
  a_all.append(a + 1)

a_counter = Counter(a_all)
print(a_counter.most_common()[0][1])