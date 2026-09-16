# 31. Set .difference() Operation

[HackerRank link](https://www.hackerrank.com/challenges/py-set-difference-operation/problem)

## What it's asking
Same English/French newspaper setup as the union and intersection problems.
This time, print how many students subscribe to the **English newspaper
only** — not French.

## Steps
1. Read both lists of roll numbers into sets.
2. Find the roll numbers in the English set that are **not** in the French
   set.
3. Print how many there are.

## Code
```python
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

print(len(english.difference(french)))
```

## Walkthrough
- `english.difference(french)` returns everything in `english` that is **not
  also** in `french`.
- Order matters here, unlike union or intersection:
  `english.difference(french)` (English-only subscribers) is not the same as
  `french.difference(english)` (French-only subscribers). Always double-check
  which set you're calling `.difference()` *on*.
- `len(...)` counts the result.
