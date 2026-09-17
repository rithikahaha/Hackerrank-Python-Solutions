# 78. Polynomials

[HackerRank link](https://www.hackerrank.com/challenges/np-polynomials/problem)

## What it's asking
Given a list of polynomial coefficients and a value `x`, evaluate the
polynomial at that `x`. The coefficients are given from the **highest**
power down to the constant term — e.g. `[1, 2, 3]` represents
`1*x² + 2*x + 3`.

## Steps
1. Read the coefficients and `x`.
2. Evaluate the polynomial at that value.
3. Print the result.

## Code
```python
import numpy

coefficients = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coefficients, x))
```

## Walkthrough
- `numpy.polyval(coefficients, x)` evaluates a polynomial at a given `x` in
  one call — it multiplies each coefficient by `x` raised to the matching
  power, and adds all those terms together.
- The order matters: the **first** coefficient goes with the **highest**
  power of `x`, counting down to the last coefficient, which is the plain
  constant term (`x⁰`). So `[1, 2, 3]` and `x = 5` computes
  `1*5² + 2*5 + 3 = 25 + 10 + 3 = 38`.
- This saves you from manually writing out
  `coefficients[0] * x**2 + coefficients[1] * x + coefficients[2]` — which
  gets tedious fast for anything beyond a couple of terms, and error-prone
  if you get an exponent wrong.
