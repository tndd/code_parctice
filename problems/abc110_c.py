from collections import Counter

S = input()
T = input()

alps_counter_s = Counter()
alps_counter_t = Counter()

for s in S:
  alps_counter_s[s] += 1

for t in T:
  alps_counter_t[t] += 1

if len(alps_counter_s.values()) == len(alps_counter_t.values()):
  print('Yes')
else:
  print('No')