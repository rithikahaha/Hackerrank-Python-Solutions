# 36. Check Strict Superset

[HackerRank link](https://www.hackerrank.com/challenges/py-check-strict-superset/problem)

## What it's asking
You're given a set `A` and then several other sets. Print `True` only if
`A` is a **strict superset** of *every one* of them — meaning `A` contains
every element of each set, **and** `A` is actually bigger than each one (not
just equal to it). If even one of them fails that, print `False`.

## Steps
1. Read set `A`.
2. Read how many other sets are coming.
3. For each one: check that `A` contains all of its elements, *and* that `A`
   has more elements than it does.
4. If every single check passes, the answer is `True`; if any one fails,
   it's `False`.

## Code
```python
A = set(map(int, input().split()))
n = int(input())

is_strict_superset = True
for _ in range(n):
    other = set(map(int, input().split()))
    if not (A.issuperset(other) and len(A) > len(other)):
        is_strict_superset = False

print(is_strict_superset)
```

## Walkthrough
- `A.issuperset(other)` checks that every element of `other` is also in `A`
  — the mirror image of `.issubset()` from the previous problem.
- Being a superset isn't quite enough for "strict," though — a set is always
  a superset of itself. `len(A) > len(other)` rules that out by requiring
  `A` to actually have more elements.
- `not (X and Y)` is `True` whenever *either* `X` or `Y` is `False` — so the
  moment one of the given sets fails either check, we flip
  `is_strict_superset` to `False` and it stays that way, since nothing later
  in the loop ever sets it back to `True`.
- We can't stop checking early even after finding one failure, because we
  still need to consume all `n` sets from the input — so the loop always
  runs to the end.
