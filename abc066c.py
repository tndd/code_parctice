n = int(input())
a = list(map(int, input().split()))

a_even = list(filter(lambda x: x % 2 == 0, a))
a_odd = list(filter(lambda x: x % 2 != 0, a))

ans = a_even[::-1] + a_odd
if n % 2 != 0:
  ans = ans[::-1]

print(' '.join(map(str, ans)))