from itertools import permutations

S, k = input().split()
k = int(k)

for perm in permutations(sorted(S), k):
    print("".join(perm))
