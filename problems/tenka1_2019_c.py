# N white and black stones.
# want to avoid a white stone on the right side of a black stone.

from collections import Counter

N = int(input())
S = list(input())
Sc = Counter(S)
min_cnt = min(Sc['.'], Sc['#'])
left_white = 0
left_black = 0
for s in S:
    if s == '.':
        left_white += 1
    else:
        left_black += 1
    right_white = Sc['.'] - left_white
    min_cnt = min(min_cnt, left_black + right_white)

print(min_cnt)
