from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted(S)

for size in range(1, k + 1):
    for combo in combinations(S, size):
        print("".join(combo))
