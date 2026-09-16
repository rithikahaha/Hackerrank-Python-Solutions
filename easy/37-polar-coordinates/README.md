# 37. Polar Coordinates

[HackerRank link](https://www.hackerrank.com/challenges/polar-coordinates/problem)

## What it's asking
You're given a complex number as text, like `1+2j`. Print its **modulus**
(distance from the origin) and its **phase** (the angle it makes, in
radians), each on its own line.

## Steps
1. Read the input and turn it into an actual Python complex number.
2. Print its modulus.
3. Print its phase.

## Code
```python
import cmath

z = complex(input())
print(abs(z))
print(cmath.phase(z))
```

## Walkthrough
- Python has a built-in `complex` number type. `complex(input())` reads text
  like `"1+2j"` and directly parses it into a complex number — no manual
  splitting on `+` needed.
- `abs(z)` on a complex number gives you its **modulus**: how far it is from
  `0` on the complex plane, calculated as `sqrt(real² + imaginary²)`. This is
  the same `abs()` you'd use for a plain number's absolute value — it just
  knows what to do with complex numbers too.
- `cmath` is a module specifically for complex-number math (as opposed to
  `math`, which only handles regular numbers). `cmath.phase(z)` gives you the
  angle, in radians, between the positive real axis and the line from the
  origin to `z`.
