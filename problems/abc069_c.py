N = int(input())
n = list(map(int, input().split()))

n4 = len(list(filter(lambda x: x % 4 == 0, n)))
no = len(list(filter(lambda x: x % 2 == 1, n)))
if n4 + no < N:
    no += 1

if no <= n4 + 1:
    print('Yes')
else:
    print('No')
    