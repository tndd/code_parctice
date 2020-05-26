def gcd(a, b):
    md = a % b
    if md == 0:
        return b
    return gcd(b, md)

def lcm(a, b):
    _gcd = gcd(a, b)
    return int((a * b) / _gcd)

def lcm_mlt(a, num_list):
    if len(num_list) == 0:
        return a
    n = num_list.pop()
    a = max(a, n)
    b = min(a, n)
    return lcm_mlt(lcm(a, b), num_list)

n = int(input())
nl = [int(input()) for _ in range(n)]

print(lcm_mlt(1, nl))