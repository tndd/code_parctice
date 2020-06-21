from collections import Counter

S = input()
T = input()

alps_counter_s = Counter(S).most_common()
alps_counter_t = Counter(T).most_common()

for s, t in zip(alps_counter_s, alps_counter_t):
    if s[1] != t[1]:
        print("No")
        break
else:
    print("Yes")
