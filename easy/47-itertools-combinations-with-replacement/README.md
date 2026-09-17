# 47. itertools.combinations_with_replacement()

[HackerRank link](https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem)

## What it's asking
Given a string `S` and a number `k`, print every possible size-`k` selection
of its characters, **allowing the same character to be picked more than
once**, in alphabetical order.

## Steps
1. Sort the letters of `S`.
2. Generate every size-`k` selection, allowing repeats.
3. Print each one.

## Code
```python
from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
S = sorted(S)

for combo in combinations_with_replacement(S, k):
    print("".join(combo))
```

## Walkthrough
- `combinations_with_replacement(iterable, r)` works just like
  `combinations()` from the previous problem, except it also allows picking
  the *same position* more than once. For `"AB"` with `k=2`, regular
  `combinations()` would only give `('A', 'B')`, but this also includes
  `('A', 'A')` and `('B', 'B')`.
- A good way to think about the difference: `combinations()` picks `r`
  *different* items from the group; `combinations_with_replacement()` picks
  `r` items where you're allowed to pick the same one again, like drawing a
  card, noting it, and putting it back before drawing again.
- Sorting `S` beforehand keeps the results in alphabetical order, same
  reasoning as the last two problems.
