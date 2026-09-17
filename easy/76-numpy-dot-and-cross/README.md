# 76. Dot and Cross

[HackerRank link](https://www.hackerrank.com/challenges/np-dot-and-cross/problem)

## What it's asking
Given two `N`-by-`N` arrays, print their **matrix product** — the actual
"multiply two matrices together" operation from linear algebra, not just
multiplying matching positions.

## Steps
1. Read both arrays.
2. Compute their matrix product.
3. Print it.

## Code
```python
import numpy

n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(a, b))
```

## Walkthrough
- `numpy.dot(a, b)` computes true **matrix multiplication**: to get the
  value at row `i`, column `j` of the result, it multiplies row `i` of `a`
  with column `j` of `b`, position by position, and adds up those products.
  This is genuinely different from `a * b` (from the "Array Mathematics"
  problem), which just multiplies matching positions and doesn't combine
  rows with columns at all.
- This is the operation actually meant when someone says "multiply two
  matrices" in linear algebra — it shows up constantly in things like
  transforming coordinates, solving systems of equations, and neural
  networks.
- Both arrays need to be square (`N`-by-`N`) here so the multiplication
  lines up cleanly — in general, matrix multiplication requires the number
  of columns in `a` to match the number of rows in `b`.
