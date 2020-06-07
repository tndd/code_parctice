H, W = list(map(int, input().split()))

ans = float('inf')

# only need to consider the horizontal length of the cut at the beginning.
# the vertical length must be cut in the center. (if possible.)
# if you cut outside of center, you will be father away from the answer.
if H % 2 == 0:
  for x in range(1, W):
    S1 = x * H
    S2 = (W - x) * (H / 2)
    ans = min(ans, abs(S1 - S2))
if W % 2 == 0:
  for x in range(1, H):
    S1 = W * x
    S2 = (H - x) * (W / 2)
    ans = min(ans, abs(S1 - S2))
else:
  # both sides are odd.
  for x in range(1, W):
    S1 = x * H
    S2 = (W - x) * (H // 2)
    S3 = (W - x) * ((H // 2) + 1)
    # if both sides are odd, three number appear.
    # it is not clear which of the three numbers is the largest or smallest, it need to be caluculated.
    S_max = max(S1, S3)
    S_min = min(S1, S2)
    ans = min(ans, S_max - S_min)
  for x in range(1, H):
    S1 = W * x
    S2 = (H - x) * (W // 2)
    S3 = (H - x) * ((W // 2) + 1)
    S_max = max(S1, S3)
    S_min = min(S1, S2)
    ans = min(ans, S_max - S_min)

# if the length or side can be trisected, then the answer is 0.
if H % 3 == 0 or W % 3 == 0:
  ans = 0

print(int(ans))