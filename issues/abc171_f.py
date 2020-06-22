K = int(input())
S = input()

ans = 1
ins_ptn = len(S) + 1
for i in range(K):
  ans *= 26 * ins_ptn
  ins_ptn += 1

print(ans % (10**9 + 7))