# 70. Zeros and Ones

[HackerRank link](https://www.hackerrank.com/challenges/np-zeros-and-ones/problem)

## What it's asking
Given a shape (some numbers describing the dimensions, e.g. `3 3` for a
3×3 grid), print an array of that shape filled entirely with `0`s, then
another one filled entirely with `1`s.

## Steps
1. Read the shape.
2. Build an array of that shape filled with zeros, and print it.
3. Build an array of that shape filled with ones, and print it.

## Code
```python
import numpy

shape = tuple(map(int, input().split()))

print(numpy.zeros(shape, dtype=int))
print(numpy.ones(shape, dtype=int))
```

## Walkthrough
- `numpy.zeros(shape)` and `numpy.ones(shape)` create brand-new arrays of a
  given shape, already filled entirely with `0`s or `1`s. This is useful as
  a starting point when you need an array of a certain size *before* you
  have real values to put in it.
- `shape` is a **tuple** like `(3, 3)` or `(2, 4, 3)`, describing how many
  dimensions the array has and how large each one is — `tuple(map(int,
  input().split()))` reads the shape numbers off one line and packages them
  together.
- `dtype=int` tells numpy to store the values as whole numbers, printed
  as `1`, rather than numpy's default floating-point form, `1.0`.
