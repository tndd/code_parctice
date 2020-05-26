def gcd(a, b):
    md = a % b
    if md == 0:
        return b
    return gcd(b, md)

def lcm(a, b):
    _gcd = gcd(a, b)
    return int((a * b) / _gcd)

n = int(input())

ans = 1
for i in range(n):
    t = int(input())
    if t >= ans:
        ans = lcm(t, ans)
    else:
        ans = lcm(ans, t)
print(ans)