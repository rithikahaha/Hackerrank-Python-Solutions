# 73. Sum and Prod

[HackerRank link](https://www.hackerrank.com/challenges/np-sum-and-prod/problem)

## What it's asking
Given an `N`-by-`M` array, add up each **column** first, then multiply all
of those column totals together into one final number.

## Steps
1. Read the array.
2. Sum down each column, giving one total per column.
3. Multiply all of those column totals together.
4. Print the result.

## Code
```python
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

col_sum = numpy.sum(arr, axis=0)
print(numpy.prod(col_sum))
```

## Walkthrough
- `numpy.sum(arr, axis=0)` adds up values **down each column** — `axis=0`
  means "collapse the rows, keep the columns separate." The result is a
  smaller, 1-dimensional array with one total per column. (This is the same
  `axis` idea from `.transpose()` and `.concatenate()` in earlier
  problems — `axis=0` operates down the rows, `axis=1` would operate across
  the columns instead.)
- `numpy.prod(col_sum)` then multiplies **all** the values in that
  column-sums array together into one single number.
- So the whole thing reads as two steps chained together: first collapse
  each column into a total, then collapse those totals into one number by
  multiplying them.
