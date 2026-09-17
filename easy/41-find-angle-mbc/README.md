# 41. Find Angle MBC

[HackerRank link](https://www.hackerrank.com/challenges/find-angle/problem)

## What it's asking
You have a right triangle `ABC`, right-angled at `B`. You're given the
lengths of the two legs, `AB` and `BC`. `M` is the midpoint of the
hypotenuse `AC`. Find the angle `MBC` (the angle at `B`, between `BM` and
`BC`), rounded to the nearest whole degree.

## Steps
This one leans on a geometry fact more than code, so the thinking happens
before you write anything:
1. In any right triangle, the midpoint of the hypotenuse is the same
   distance from all three corners — so `BM = AM = CM`.
2. That makes triangle `BMC` isosceles (`BM = CM`), which means its two base
   angles are equal: `angle MBC = angle MCB`.
3. `angle MCB` is just `angle ACB` — the same angle, since `M` sits on line
   `AC`.
4. So the whole problem reduces to: what's `angle C` in the original right
   triangle? That's a plain trig calculation using `AB` and `BC`.

## Code
```python
import math

AB = int(input())
BC = int(input())

angle = math.degrees(math.atan(AB / BC))
print(f"{round(angle)}°")
```

## Walkthrough
- In right triangle `ABC` (right angle at `B`), angle `C`'s opposite side is
  `AB` and its adjacent side is `BC`, so `tan(C) = AB / BC`.
- `math.atan(...)` is the inverse of tangent — give it a ratio, it gives you
  back the angle (in radians) that produces that ratio.
- `math.degrees(...)` converts that radians value into degrees, which is
  what humans (and this problem) expect.
- `round(angle)` rounds to the nearest whole number, and the f-string tacks
  the `°` symbol onto the end.
- The one-sentence version to remember: **`angle MBC` turns out to equal
  `angle C`** of the original triangle, thanks to the isosceles triangle
  formed by the median to the hypotenuse.
