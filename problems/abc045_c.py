from itertools import product
S = input()

# is insert + on the right side.
patterns = product([True, False], repeat=len(S)-1)

ans = 0
for ptn in patterns:
  ptn_idxs = [i for i, bl in enumerate(ptn) if bl]
  ptn_s = ''
  for i in range(len(S) - 1):
    ptn_s += S[i]
    if i in ptn_idxs:
      ptn_s += '+'
  ans += eval(ptn_s + S[-1])

print(ans)
