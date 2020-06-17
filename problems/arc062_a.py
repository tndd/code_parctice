N = int(input())
T = []
A = []

for _ in range(N):
    t, a = list(map(int, input().split()))
    T.append(t)
    A.append(a)

t_num = 1
a_num = 1
for i in range(N):
    # TAは常にn倍ずつ増加していく
    n = 1
    while T[i] * n < t_num or A[i] * n < a_num:
        n += 1
    t_num = T[i] * n
    a_num = A[i] * n

print(t_num + a_num)


# 2:3
# 3:5 <- そのまま増加

# 3:5
# @5:3 左右の大小が逆転した場合
# (25/3):5になればいい
