n = int(input())
a = list(map(int, input().split()))

a_even = [elm_a for i, elm_a in enumerate(a) if i % 2 == 0]
a_odd = [elm_a for i, elm_a in enumerate(a) if i % 2 == 1]

ans = a_even[::-1] + a_odd
if n % 2 == 0:
  ans = ans[::-1]

print(' '.join(map(str, ans)))