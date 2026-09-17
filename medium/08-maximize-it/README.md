# 8. Maximize It!

[HackerRank link](https://www.hackerrank.com/challenges/maximize-it/problem)

## What it's asking
You're given `K` lists of numbers, and a modulus `M`. Pick **exactly one**
number from each list, square each chosen number, add all the squares
together, and take that total modulo `M`. Out of every possible way to make
those `K` picks, find the **largest** result you can get.

## Steps
1. Read all `K` lists.
2. Generate every possible way to pick one number from each list.
3. For each combination, compute the sum of squares, then take it modulo
   `M`.
4. Keep track of the biggest result seen across every combination.

## Code
```python
from itertools import product

K, M = map(int, input().split())

arrays = []
for _ in range(K):
    parts = list(map(int, input().split()))
    arrays.append(parts[1:])

max_value = 0
for combo in product(*arrays):
    value = sum(x ** 2 for x in combo) % M
    max_value = max(max_value, value)

print(max_value)
```

## Walkthrough
- Each input line starts with a count, followed by that many numbers (e.g.
  `"3 7 8 9"` means "3 numbers: 7, 8, 9"). `parts[1:]` drops that leading
  count and keeps only the actual numbers — we don't need the count itself
  in Python, since we can just use the rest of the list directly.
- `itertools.product(*arrays)` generates every possible way to pick exactly
  one number from each of the `K` lists — the same "Cartesian product" idea
  from problem 44 in the Easy section, just extended from two lists to
  however many `arrays` contains, using `*` to unpack them all as separate
  arguments.
- For each combination, `sum(x ** 2 for x in combo)` squares every chosen
  number and adds the squares together, then `% M` takes that total modulo
  `M`.
- `max_value = max(max_value, value)` keeps a running "biggest value seen
  so far," checked after every single combination — by the time the loop
  finishes, it holds the maximum across *all* of them.
- Since the constraints keep the lists small (at most 7 items each), the
  total number of combinations stays manageable even though this checks
  every single one — a full brute-force search is genuinely the intended
  approach here, not just a shortcut.
