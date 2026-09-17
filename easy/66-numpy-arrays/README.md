# 66. Arrays

[HackerRank link](https://www.hackerrank.com/challenges/np-arrays/problem)

## What it's asking
Given space-separated numbers, build a **numpy array** from them, but in
**reverse order**, and print it.

This starts the **Numpy** section — `numpy` is a library built for fast,
efficient work with arrays of numbers. It's used constantly in data
analysis and scientific computing, so it's worth getting comfortable with
even at this basic level.

## Steps
1. Read the numbers as a list of text values.
2. Reverse the list.
3. Turn it into a numpy array of floats.
4. Print it.

## Code
```python
import numpy


def arrays(arr):
    return numpy.array(arr[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)
```

## Walkthrough
- `input().strip().split(' ')` reads the line and breaks it into a list of
  text pieces, same pattern you've used throughout — `.strip()` just clears
  any stray whitespace at the ends of the line first.
- `arr[::-1]` reverses the list — the same slicing trick used for reversing
  strings earlier in this repo.
- `numpy.array(list, float)` converts a plain Python list into a numpy
  array, converting every value to a `float` in the process.
- Printing a numpy array looks a little different from a plain list — no
  commas between the numbers, right-aligned, shown with decimal points.
  That's numpy's own formatting, built for reading numeric data clearly, not
  a bug or a mistake.
