# 74. Min and Max

[HackerRank link](https://www.hackerrank.com/challenges/np-min-and-max/problem)

## What it's asking
Given an `N`-by-`M` array, find the **smallest** value in each row, then
print the **largest** value among those row-minimums.

## Steps
1. Read the array.
2. Find the minimum value in each row.
3. Find the maximum among those minimums.
4. Print it.

## Code
```python
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

row_min = numpy.min(arr, axis=1)
print(numpy.max(row_min))
```

## Walkthrough
- `numpy.min(arr, axis=1)` finds the smallest value in each **row** —
  `axis=1` means "collapse the columns, going across each row." The result
  is one minimum value per row.
- `numpy.max(row_min)` then finds the biggest value among those per-row
  minimums.
- Put together: this finds "the largest of the smallest values in each
  row" — a genuinely common two-step pattern once you're comfortable
  choosing which axis to operate along (this is the mirror image of the
  previous problem, which summed down columns rather than finding minimums
  across rows).
