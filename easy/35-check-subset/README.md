# 35. Check Subset

[HackerRank link](https://www.hackerrank.com/challenges/py-check-subset/problem)

## What it's asking
You're given several test cases. Each one has two sets, `A` and `B`. Print
`True` if every element of `A` is also in `B` (meaning `A` is a **subset**
of `B`), otherwise `False`.

## Steps
1. Read how many test cases there are.
2. For each one, read set `A` and set `B`.
3. Check whether `A` is a subset of `B` and print the result.

## Code
```python
T = int(input())
for _ in range(T):
    a_count = int(input())
    A = set(map(int, input().split()))
    b_count = int(input())
    B = set(map(int, input().split()))
    print(A.issubset(B))
```

## Walkthrough
- `A.issubset(B)` returns `True` if **every** element in `A` can also be
  found in `B`, and `False` if even one element of `A` is missing from `B`.
- `a_count` and `b_count` just tell you how many numbers are on the next
  line — we read them but don't need to use them directly, since
  `input().split()` already reads the whole line regardless.
- This is a nice complement to `.issuperset()` (used in the next problem) —
  `A.issubset(B)` and `B.issuperset(A)` are actually asking the exact same
  question, just from opposite directions.
