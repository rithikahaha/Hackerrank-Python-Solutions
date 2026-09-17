# 67. Shape and Reshape

[HackerRank link](https://www.hackerrank.com/challenges/np-shape-reshape/problem)

## What it's asking
Given 9 space-separated integers, rearrange them into a 3-row-by-3-column
grid and print it.

## Steps
1. Read the 9 numbers into a numpy array.
2. Reshape that array into 3 rows and 3 columns.
3. Print it.

## Code
```python
import numpy

arr = numpy.array(input().split(), int)
print(arr.reshape(3, 3))
```

## Walkthrough
- `numpy.array(input().split(), int)` reads the line, splits it into
  separate values, and builds a 1-dimensional numpy array of whole numbers
  from them.
- `.reshape(3, 3)` rearranges those same 9 numbers into a 3×3 grid — 3 rows,
  3 columns. Reshaping doesn't change any of the values or their order, it
  only changes how they're grouped: the array fills the new shape row by
  row, left to right, top to bottom.
- The total number of values has to match the new shape exactly — 9 numbers
  fits a 3×3 grid (`3 × 3 = 9`) perfectly; you couldn't reshape 9 numbers
  into a 4×4 grid, since that needs 16.
