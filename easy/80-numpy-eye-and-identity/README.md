# 80. Eye and Identity

[HackerRank link](https://www.hackerrank.com/challenges/numpy-eye-and-identity/problem)

## What it's asking
Given `N` and `M`, print an `N`-by-`M` array that's mostly zeros, except for
`1`s running diagonally from the top-left corner. (When `N` equals `M`,
this specific pattern is called an **identity matrix**.)

## Steps
1. Read `N` and `M`.
2. Build the array with numpy's built-in tool for exactly this shape.
3. Print it.

## Code
```python
import numpy

numpy.set_printoptions(legacy='1.13')

n, m = map(int, input().split())
print(numpy.eye(n, m))
```

## Walkthrough
- `numpy.eye(n, m)` builds this diagonal pattern directly — no loops
  needed. Every position gets a `0`, except positions where the row number
  equals the column number, which get a `1`.
- `numpy.set_printoptions(legacy='1.13')` tells numpy to format its printed
  numbers the way an older numpy version did. This matters here specifically
  because HackerRank's expected output was generated against that older
  formatting — without this line, a modern numpy might print the same
  numbers slightly differently (extra or missing spacing), and the exact
  text wouldn't match even though the actual values are correct.
- This is a good real-world lesson to file away: a library's *values* can be
  right while its *display formatting* differs across versions — worth
  remembering the next time output "looks wrong" but the underlying numbers
  are actually fine.
