# 40. Integers Come In All Sizes

[HackerRank link](https://www.hackerrank.com/challenges/python-integers-come-in-all-sizes/problem)

## What it's asking
Given four integers `a`, `b`, `c`, `d`, compute and print `a**b + c**d`.
That's genuinely the whole problem — the point isn't the math, it's what
happens when the numbers get big.

## Steps
1. Read `a`, `b`, `c`, `d`.
2. Compute `a ** b + c ** d`.
3. Print it.

## Code
```python
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a ** b + c ** d)
```

## Walkthrough
- There's no trick to the calculation itself — `**` is the power operator
  you've already used, and `+` just adds the two results.
- The real point of this problem: in many languages, numbers have a fixed
  size limit, and something like `a ** b` can silently "overflow" and give
  you a wrong, wrapped-around answer if it gets too big. **Python integers
  don't have that limit** — they grow automatically to fit however large the
  number actually is, even if it ends up hundreds of digits long. You don't
  need to do anything special; regular `int` just handles it.
