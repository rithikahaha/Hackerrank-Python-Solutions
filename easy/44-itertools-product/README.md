# 44. itertools.product()

[HackerRank link](https://www.hackerrank.com/challenges/itertools-product/problem)

## What it's asking
Given two lists, `A` and `B`, print every possible pair `(a, b)` — one from
each list — all on one line, space-separated. This is the **Cartesian
product** of the two lists.

## Steps
1. Read both lists.
2. Generate every combination of one item from `A` with one item from `B`.
3. Print them all on one line.

## Code
```python
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*product(A, B))
```

## Walkthrough
- `itertools` is a standard-library module full of tools for looping in
  useful patterns, so you don't have to hand-write them.
- `product(A, B)` gives you every pair `(a, b)` with `a` from `A` and `b`
  from `B` — the same result you'd get from writing
  `for a in A: for b in B: ...` yourself, just built in and ready to use.
- `print(*product(A, B))` uses `*` to **unpack** the sequence of tuples into
  separate arguments for `print`. Without the `*`, `print` would show the
  whole thing as one object; with it, each tuple gets printed
  space-separated on the same line, which is the format this problem wants.
