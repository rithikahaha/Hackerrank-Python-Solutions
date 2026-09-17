# 68. Transpose and Flatten

[HackerRank link](https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem)

## What it's asking
Given an `N`-by-`M` grid of numbers, print two things:
1. Its **transpose** — rows and columns swapped
2. Its **flattened** version — all the values squashed into one flat line

## Steps
1. Read `N` and `M`, then read the `N` rows of numbers into a 2D array.
2. Print the transposed version.
3. Print the flattened version.

## Code
```python
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(arr.transpose())
print(arr.flatten())
```

## Walkthrough
- `[input().split() for _ in range(n)]` reads `n` lines, splitting each one
  into a list of values — giving a list of lists, one per row.
  `numpy.array(..., int)` turns that into a proper 2D numpy array.
- `.transpose()` flips the array over its diagonal: what used to be a row
  becomes a column, and vice versa. An array with `n` rows and `m` columns
  becomes one with `m` rows and `n` columns, with the same values, just
  reorganized.
- `.flatten()` does something different: it takes a multi-dimensional array
  and collapses it down into a single, 1-dimensional list of every value,
  read out row by row, left to right, top to bottom.
- These two are genuinely different operations — transpose keeps the data
  2-dimensional but reorients it, while flatten reduces the dimensions
  entirely.
