from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combos = list(combinations(letters, k))
combos_with_a = [c for c in all_combos if 'a' in c]

probability = len(combos_with_a) / len(all_combos)
print(probability)
