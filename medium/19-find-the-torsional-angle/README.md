# 19. Class 2 - Find the Torsional Angle

[HackerRank link](https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem)

## What it's asking
Given four points in 3D space — `A`, `B`, `C`, `D` — find the **torsional
(dihedral) angle**: the angle between the plane through `A`, `B`, `C` and
the plane through `B`, `C`, `D`. This is a real calculation used in
chemistry to describe the "twist" of a molecule's structure.

## Steps
1. Build a `Points` class that can represent an (x, y, z) coordinate and
   support the vector operations we'll need: subtraction, cross product,
   dot product, and magnitude.
2. Find a vector pointing "along" each of the two planes.
3. Take the cross product of those vectors to get each plane's **normal**
   (a vector pointing straight out of the plane).
4. Use the angle-between-two-vectors formula on the two normals — that
   angle **is** the angle between the planes.

## Code
```python
import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        return Points(self.x - no.x, self.y - no.y, self.z - no.z)

    def dot(self, no):
        return self.x * no.x + self.y * no.y + self.z * no.z

    def cross(self, no):
        return Points(
            self.y * no.z - self.z * no.y,
            self.z * no.x - self.x * no.z,
            self.x * no.y - self.y * no.x,
        )

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)

    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
```

## Walkthrough
- The `Points` class bundles an (x, y, z) coordinate with the vector
  operations needed to work with it:
  - `__sub__` (the `-` operator) between two points gives the **vector**
    pointing from one to the other.
  - `.cross(other)` computes the **cross product** — a new vector that
    points perpendicular to both of the original two. This matters here
    because the cross product of two vectors that lie *in* a plane gives
    you that plane's **normal** (a vector sticking straight out of it).
  - `.dot(other)` computes the **dot product** — a single number, related
    to the angle between two vectors.
  - `.absolute()` computes a vector's **magnitude** (length), using the
    standard 3D distance formula, `sqrt(x² + y² + z²)`.
- `(b - a).cross(c - b)` finds the normal vector for the plane through
  `A`, `B`, `C` — using two vectors that both lie in that plane (`B - A`
  and `C - B`).
- `(c - b).cross(d - c)` does the same for the plane through `B`, `C`, `D`.
- The angle between two vectors `x` and `y` follows a standard formula:
  `cos(angle) = (x · y) / (|x| · |y|)` — the dot product divided by the
  product of their magnitudes. `math.acos(...)` reverses that, turning a
  cosine value back into the actual angle, in radians.
- `math.degrees(...)` converts radians to degrees (the unit humans actually
  read), and `"%.2f" %` formats the result to 2 decimal places.
