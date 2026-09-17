# 9. Classes: Dealing with Complex Numbers

[HackerRank link](https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem)

## What it's asking
Build a `Complex` class representing a complex number (a real part plus an
imaginary part), and make it support `+`, `-`, `*`, `/`, and a `.mod()`
method for its modulus (distance from `0`) — then print the results in a
specific format like `3.00+4.00i`.

## Steps
1. Store a complex number's real and imaginary parts when one is created.
2. Define what each operator (`+`, `-`, `*`, `/`) should actually compute,
   using the standard rules of complex number arithmetic.
3. Define `.mod()` to compute the distance from `0`.
4. Define how a `Complex` object should be displayed as text, matching the
   exact expected format.

## Code
```python
import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)

    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)

    def __mul__(self, no):
        real = self.real * no.real - self.imaginary * no.imaginary
        imaginary = self.real * no.imaginary + self.imaginary * no.real
        return Complex(real, imaginary)

    def __truediv__(self, no):
        denom = no.real ** 2 + no.imaginary ** 2
        real = (self.real * no.real + self.imaginary * no.imaginary) / denom
        imaginary = (self.imaginary * no.real - self.real * no.imaginary) / denom
        return Complex(real, imaginary)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')
```

## Walkthrough
- A **class** is a blueprint for creating objects that bundle related data
  and behavior together. `__init__` is the constructor — it runs
  automatically every time you write `Complex(real, imaginary)`, and its
  job is to save the values onto the new object (`self.real = real`).
- `__add__`, `__sub__`, `__mul__`, and `__truediv__` are **operator
  overloading** — special ("dunder," short for double-underscore) method
  names that Python calls automatically when you use `+`, `-`, `*`, `/` on
  your own objects. Write `x + y` where `x` is a `Complex`, and Python calls
  `x.__add__(y)` behind the scenes, instead of trying (and failing at)
  regular number addition.
- The actual math inside each method — `real * no.real - imaginary *
  no.imaginary` for multiplication, and the more involved formula for
  division — comes directly from the standard rules of complex number
  arithmetic (built on the fact that `i * i = -1`). These formulas aren't
  something to derive yourself; they're just applied as-is.
- `.mod()` computes the modulus (distance from the origin) using the same
  `sqrt(real² + imaginary²)` idea as "Polar Coordinates" in the Easy
  section — then wraps it in a `Complex` with `0` imaginary part, since the
  problem expects the modulus printed in the same `"x.xx+0.00i"` format as
  everything else.
- `__str__` controls what `print(x)` actually shows. Without it, printing a
  custom object would display something unhelpful like a memory address.
  This one has several branches purely to match the exact expected text
  format — e.g. `"0.00-2.00i"` needs `abs()` around the imaginary part so
  the sign shows up as a `-` in the right spot, rather than a raw negative
  number after a `+`.
