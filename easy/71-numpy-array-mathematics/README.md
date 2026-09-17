# 71. Array Mathematics

[HackerRank link](https://www.hackerrank.com/challenges/np-array-mathematics/problem)

## What it's asking
Given two `N`-by-`M` arrays, `A` and `B`, print the result of adding,
subtracting, multiplying, dividing, and raising them to each other's power —
all **element by element** (matching position to matching position).

## Steps
1. Read both arrays.
2. Print `A + B`, `A - B`, `A * B`, `A // B`, `A % B`, `A ** B`, in that
   order.

## Code
```python
import numpy

n, m = map(int, input().split())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(a ** b)
```

## Walkthrough
- This is one of numpy's biggest advantages over plain Python lists: normal
  math operators (`+`, `-`, `*`, `//`, `%`, `**`) work **directly** on whole
  arrays, applying the operation to every matching pair of positions at
  once. `a + b` doesn't glue the two arrays together like it would for
  lists — it adds each corresponding value together.
- Doing this by hand with plain lists would mean writing a nested loop over
  every position yourself; numpy does it in one line, and does it fast.
- `a // b` is elementwise integer division, `a % b` is elementwise
  remainder, and `a ** b` raises each value in `a` to the power of the
  matching value in `b` — all the same operators you already know from
  single numbers, just spread automatically across the whole array.
