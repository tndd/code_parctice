from collections import Counter

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

A_counter = Counter(A)
A_sum = sum(A)

for _ in range(Q):
    b, c = list(map(int, input().split()))
    inc_num = A_counter[b] * (c - b)
    A_sum += inc_num
    print(A_sum)
    A_counter[c] += A_counter[b]
    A_counter[b] = 0