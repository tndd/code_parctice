candi_num, can_exist_num = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0

# first candi
ofs = max(0, A[0] + A[1] - can_exist_num)
if ofs > A[1]:
  A[0] -= ofs - A[1]
  ans += ofs - A[1]

for i in range(1, candi_num):
  two_sum = A[i - 1] + A[i]
  ofs = max(0, two_sum - can_exist_num)
  A[i] -= ofs
  ans += ofs

print(ans)