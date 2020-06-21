from collections import Counter

n = int(input())
v = list(map(int, input().split()))

even_counter = Counter()
odd_counter = Counter()
for i in range(n):
  if i % 2 == 0:
    even_counter[v[i]] += 1
  else:
    odd_counter[v[i]] += 1

even_num = n//2
odd_num = (n + 2 - 1)//2

evens = even_counter.most_common(2)
odds = odd_counter.most_common(2)

if evens[0][0] == odds[0][0]:
  if len(evens) == 1 and len(odds) == 1:
    print(even_num)
  elif len(evens) > 1 and len(odds) == 1:
    ans_even = even_num - evens[1][1]
    ans_odd = odd_num - odds[0][1]
    print(ans_even + ans_odd)
  elif len(evens) == 1 and len(odds) > 1:
    ans_even = even_num - evens[0][1]
    ans_odd = odd_num - odds[1][1]
    print(ans_even + ans_odd)
  elif len(evens) > 1 and len(odds) > 1:
    if even_num - evens[1][1] >= odd_num - odds[1][1]:
      ans_even = even_num - evens[0][1]
      ans_odd = odd_num - odds[1][1]
      print(ans_even + ans_odd)
    else:
      ans_even = even_num - evens[1][1]
      ans_odd = odd_num - odds[0][1]
      print(ans_even + ans_odd)
else:
  ans_even = even_num - evens[0][1]
  ans_odd = odd_num - odds[0][1]
  print(ans_even + ans_odd)
