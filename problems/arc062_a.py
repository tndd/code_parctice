from math import ceil

N = int(input())
T = []
A = []

for _ in range(N):
    t, a = list(map(int, input().split()))
    T.append(t)
    A.append(a)

t_num = T[0]
a_num = A[0]
for i in range(1, N):
    tn = (t_num + T[i] - 1) // T[i]
    an = (a_num + A[i] - 1) // A[i]
    n = max(tn, an)
    t_num = T[i] * n
    a_num = A[i] * n

print(t_num + a_num)
