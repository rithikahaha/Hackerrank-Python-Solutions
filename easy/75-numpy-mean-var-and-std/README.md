# 75. Mean, Var, and Std

[HackerRank link](https://www.hackerrank.com/challenges/np-mean-var-and-std/problem)

## What it's asking
Given an `N`-by-`M` array, print:
1. The average (**mean**) of each **row**
2. The **variance** of each **column**
3. The **standard deviation** of the entire array, as one number

## Steps
1. Read the array.
2. Compute the mean across each row.
3. Compute the variance down each column.
4. Compute the standard deviation of everything, treated as one group.

## Code
```python
import numpy

n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(numpy.std(arr))
```

## Walkthrough
- **Mean** is just the average — add up the values, divide by how many
  there are.
- **Variance** measures how spread out a group of numbers is from their
  average — a bigger variance means the values are more scattered.
- **Standard deviation** is the square root of the variance — another way
  to describe spread, but back in the same units as the original data
  (variance's units are "squared," which makes it less intuitive to
  interpret directly).
- `numpy.mean(arr, axis=1)` averages **across** each row (`axis=1`),
  giving one mean per row.
- `numpy.var(arr, axis=0)` computes variance **down** each column
  (`axis=0`), giving one variance value per column.
- `numpy.std(arr)` — with **no** `axis` argument — treats the *entire*
  array as a single group of numbers and returns just one overall standard
  deviation, rather than a per-row or per-column result.
