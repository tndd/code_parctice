N = int(input())

# factorial
Nf = 1
for i in range(2, N + 1):
  Nf *= i

print(Nf)

# divisor num
Ndn = 0
for i in range(1, Nf // 2 + 1):
  if Nf % i == 0:
    Ndn += 1

# plus self num
print(Ndn + 1 % (10**9 + 7))
