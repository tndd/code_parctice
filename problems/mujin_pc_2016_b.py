from math import pi

l = sorted(list(map(int, input().split())), reverse=True)

s = pi * sum(l)**2
if l[0] <= l[1] + l[2]:
    print(s)
else:
    s_short = pi * (l[0] - l[1] - l[2])**2
    print(s - s_short)
