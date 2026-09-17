# 7. Iterables and Iterators

[HackerRank link](https://www.hackerrank.com/challenges/iterables-and-iterators/problem)

## What it's asking
Given a list of `N` letters and a number `K`, if you picked `K` letters at
random from the list (order doesn't matter, no repeats), what's the
**probability** that your selection contains at least one `'a'`?

## Steps
1. Generate every possible way to pick `K` letters from the list — that's
   the full set of equally-likely outcomes.
2. Count how many of those selections contain at least one `'a'`.
3. Divide that count by the total number of selections — that's the
   probability.

## Code
```python
from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combos = list(combinations(letters, k))
combos_with_a = [c for c in all_combos if 'a' in c]

probability = len(combos_with_a) / len(all_combos)
print(probability)
```

## Walkthrough
- `combinations(letters, k)` generates **every** possible way to choose `k`
  letters from the list, without regard to order. Since each one is an
  equally likely outcome of "randomly picking k letters," this list *is*
  the complete sample space the probability is calculated over.
- `'a' in c` checks whether a given combination (a tuple of letters)
  contains at least one `'a'` — the same `in` membership check used
  throughout this repo, just applied to a tuple instead of a string or
  dictionary.
- Probability, by definition, is `favorable outcomes / total outcomes`.
  `len(combos_with_a)` counts the favorable ones (contains an `'a'`);
  `len(all_combos)` counts all of them. Dividing gives exactly that
  probability.
- Note that if the input list has **duplicate** letters (like two separate
  `'a'`s), `combinations()` still treats them as distinct items based on
  their position in the list — which correctly matches "randomly drawing
  physical letter tiles," where two tiles that happen to show the same
  letter are still two different tiles.
