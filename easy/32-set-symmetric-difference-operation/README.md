# 32. Set .symmetric_difference() Operation

[HackerRank link](https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem)

## What it's asking
Same English/French setup again. Print how many students subscribe to
**exactly one** of the two newspapers (English only, or French only — not
both).

## Steps
1. Read both lists into sets.
2. Find everything that's in exactly one of the two sets.
3. Print how many there are.

## Code
```python
n = int(input())
english = set(map(int, input().split()))
m = int(input())
french = set(map(int, input().split()))

print(len(english.symmetric_difference(french)))
```

## Walkthrough
- `.symmetric_difference()` returns everything that's in one set or the
  other, but **not in both** — you saw this method already in problem 26,
  just printed as a sorted list there instead of a count.
- Compare all four set operations you now know, side by side:
  - `.union()` — in either set (problem 29)
  - `.intersection()` — in both sets (problem 30)
  - `.difference()` — in this set but not the other (problem 31)
  - `.symmetric_difference()` — in one set but not both (this one)
- `len(...)` gives the final count.
