N = int(input())
n = list(map(int, input().split()))

nfl = len(list(filter(lambda x: x%4==0, n)))

if (N / 3) <= nfl:
    print('Yes')
else:
    print('No')