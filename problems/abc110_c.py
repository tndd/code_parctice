from collections import Counter

S = input()
T = input()

st = {}
ts = {}

for s, t in zip(S, T):
  if s not in st:
    st[s] = t
  else:
    if st[s] != t:
      print('No')
      break
  if t not in ts:
    ts[t] = s
  else:
    if ts[t] != s:
      print('No')
      break
else:
  print('Yes')