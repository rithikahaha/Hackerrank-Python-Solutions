# 46. itertools.combinations()

[HackerRank link](https://www.hackerrank.com/challenges/itertools-combinations/problem)

## What it's asking
Given a string `S` and a number `k`, print every possible **selection**
(order doesn't matter) of characters from `S`, for every size from `1` up to
`k` — smallest size first, in alphabetical order.

## Steps
1. Sort the letters of `S` so results come out alphabetically.
2. For each size from `1` to `k`, generate every possible selection of that
   size.
3. Print each one.

## Code
```python
from itertools import combinations

S, k = input().split()
k = int(k)
S = sorted(S)

for size in range(1, k + 1):
    for combo in combinations(S, size):
        print("".join(combo))
```

## Walkthrough
- `combinations(iterable, r)` gives every possible way to **pick** `r` items
  from `iterable`, without caring about order — `"AB"` and `"BA"` count as
  the same selection, so only one of them shows up. This is the key
  difference from `permutations()` in the previous problem.
- Sorting `S` first, same as before, makes the output come out in
  alphabetical order automatically.
- The outer loop (`for size in range(1, k + 1)`) makes sure we print all the
  size-`1` selections first, then all the size-`2` selections, and so on up
  to size `k` — matching the order the problem expects.
- `"".join(combo)` turns each tuple of characters back into a plain string
  for printing.
