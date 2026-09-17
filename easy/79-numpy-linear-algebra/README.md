# 79. Linear Algebra

[HackerRank link](https://www.hackerrank.com/challenges/np-linear-algebra/problem)

## What it's asking
Given an `N`-by-`N` array, print its **determinant** — a single number with
several important uses in linear algebra, rounded to 2 decimal places.

## Steps
1. Read the array.
2. Compute its determinant.
3. Round it and print it.

## Code
```python
import numpy

n = int(input())
arr = numpy.array([input().split() for _ in range(n)], float)

print(round(numpy.linalg.det(arr), 2))
```

## Walkthrough
- `numpy.linalg` is a sub-module built specifically for **linear algebra**
  operations — things like determinants, matrix inverses, and solving
  systems of equations. You've already used the more general parts of
  `numpy`; this is its more specialized toolbox.
- `numpy.linalg.det(arr)` computes the **determinant** of a square matrix.
  One useful fact about it: a determinant of `0` means the matrix *can't*
  be inverted — a detail that matters a lot once you get into more advanced
  math or machine learning work.
- `round(..., 2)` rounds the result to 2 decimal places. This isn't just
  cosmetic — determinant calculations often produce tiny floating-point
  rounding artifacts (like `6.999999999999998` instead of a clean `7.0`),
  and rounding cleans that up to match what's actually expected.
