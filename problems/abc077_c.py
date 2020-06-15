from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
# fix the center and find the combination of the top and bottom levels.
for i in range(N):
  # it must not contain the same number as B[i], so use bisect_left.
  cand_num_a = bisect_left(A, B[i])
  # it needs to contain the same number as B[i], so use bisect_right.
  cand_num_c = N - bisect_right(C, B[i])
  ans += cand_num_a * cand_num_c

print(ans)