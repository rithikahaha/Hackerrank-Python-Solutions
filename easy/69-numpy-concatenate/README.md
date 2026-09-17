# 69. Concatenate

[HackerRank link](https://www.hackerrank.com/challenges/np-concatenate/problem)

## What it's asking
You're given two grids of numbers: one with `N` rows, one with `M` rows,
but both with the same number of columns, `P`. Stack them together into one
combined grid with `N + M` rows, and print it.

## Steps
1. Read `N`, `M`, `P`, then read both grids.
2. Stack the second grid underneath the first.
3. Print the combined result.

## Code
```python
import numpy

n, m, p = map(int, input().split())
array_1 = numpy.array([input().split() for _ in range(n)], int)
array_2 = numpy.array([input().split() for _ in range(m)], int)

print(numpy.concatenate((array_1, array_2), axis=0))
```

## Walkthrough
- `numpy.concatenate((a, b), axis=0)` joins two arrays together along a
  chosen **axis** — a direction along which the data is organized.
  `axis=0` means "stack along the rows," i.e. add `b`'s rows underneath
  `a`'s rows. (`axis=1` would instead glue them side by side, adding more
  columns — not what we want here.)
- This only works because both arrays already share the same number of
  columns (`p`) — you can only stack rows on top of each other cleanly if
  every row is the same length; numpy would raise an error otherwise.
- The result has `n + m` rows and still `p` columns — all of `array_1`'s
  rows, followed by all of `array_2`'s rows, in order.
