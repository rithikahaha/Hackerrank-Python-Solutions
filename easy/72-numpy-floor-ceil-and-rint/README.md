# 72. Floor, Ceil and Rint

[HackerRank link](https://www.hackerrank.com/challenges/np-floor-ceil-and-rint/problem)

## What it's asking
Given an array of decimal numbers, print three versions of it:
1. Every value rounded **down**
2. Every value rounded **up**
3. Every value rounded to the **nearest** whole number

## Steps
1. Read the array.
2. Apply each of the three rounding rules to the whole array at once.
3. Print all three results.

## Code
```python
import numpy

arr = numpy.array(input().split(), float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))
```

## Walkthrough
- `numpy.floor(arr)` rounds every value **down** to the nearest whole
  number — `2.7` becomes `2.0`, and importantly, `-2.3` becomes `-3.0` (down
  means toward negative infinity, not just "drop the decimal part").
- `numpy.ceil(arr)` rounds every value **up** — `2.1` becomes `3.0`.
- `numpy.rint(arr)` rounds to the **nearest** whole number using standard
  rounding rules — `2.4` becomes `2.0`, `2.6` becomes `3.0`.
- All three apply to every element of the array in one call — no loop
  needed — and each returns a brand-new array of the same shape, still
  holding floats (`2.0`, not `2`), since that's what these functions always
  return.
