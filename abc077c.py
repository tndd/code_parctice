from bisect import bisect_left, bisect_right

N = int(input())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
C = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
  cand_num_a = bisect_left(A, B[i])
  cand_num_c = N - bisect_right(C, B[i])
  ans += cand_num_a * cand_num_c

print(ans)