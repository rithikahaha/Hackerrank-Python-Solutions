# 77. Inner and Outer

[HackerRank link](https://www.hackerrank.com/challenges/np-inner-and-outer/problem)

## What it's asking
Given two 1-dimensional arrays, `A` and `B`, print:
1. Their **inner product** — a single number
2. Their **outer product** — a full grid of every possible pairing

## Steps
1. Read both arrays.
2. Compute and print the inner product.
3. Compute and print the outer product.

## Code
```python
import numpy

a = numpy.array(input().split(), int)
b = numpy.array(input().split(), int)

print(numpy.inner(a, b))
print(numpy.outer(a, b))
```

## Walkthrough
- `numpy.inner(a, b)` multiplies matching positions together and adds all
  those products up into a **single number**. For two 1-D arrays, this is
  the same idea as the dot product you saw in the previous problem.
- `numpy.outer(a, b)` does something different: it builds a full 2-D grid
  where **every** value in `a` gets multiplied by **every** value in `b` —
  not just matching positions. The result has as many rows as `a` has
  values, and as many columns as `b` has values.
- A useful way to remember the difference: inner "combines everything down
  into one number," outer "expands out into every possible pairing."
