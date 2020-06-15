from collections import Counter

N = int(input())

THE_NUMBER = 10**9 + 7
prime_number_counter = Counter()

# factorial sequence.
for current_factorial_number in range(2, N + 1):
  # prime number calculation.
  cfn_holder = current_factorial_number
  for candidate_prime_number in range(2, current_factorial_number + 1):
    while cfn_holder % candidate_prime_number == 0:
      cfn_holder /= candidate_prime_number
      prime_number_counter[candidate_prime_number] += 1

answer = 1
for prime_number_count in prime_number_counter.values():
  answer *= prime_number_count + 1

print(answer % THE_NUMBER)