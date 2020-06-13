from collections import Counter
from math import ceil

N = int(input())
A = list(map(int, input().split()))

# a position where a person could be located.
possibility = ([0 for i in range(N)])

THE_NUM = 10**9 + 7

# testimony
for a in A:
  # to find the number of reordering, you can only count one side.
  place_left = (N - 1 - a) // 2
  possibility[place_left] += 1

answer = 1
# there is no need to count the center.
for i in range(N // 2):
  answer *= possibility[i]

# it is consistent to have more than two numbers in the middle.
if N % 2 == 1 and possibility[N//2] >= 2:
  print(0)
else:
  print(answer)