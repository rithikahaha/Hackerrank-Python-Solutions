# 39. Power - Mod Power

[HackerRank link](https://www.hackerrank.com/challenges/python-power-mod-power/problem)

## What it's asking
Given `a`, `b`, and `m`, print:
1. `a` raised to the power `b`
2. `(a ** b) % m` — but computed in a way that stays fast even when `b` is
   huge

## Steps
1. Read `a`, `b`, `m`.
2. Print `a` to the power `b`.
3. Print `a` to the power `b`, taken modulo `m` — using the 3-argument form
   of `pow()` rather than computing `a ** b` first and applying `% m` after.

## Code
```python
a = int(input())
b = int(input())
m = int(input())

print(pow(a, b))
print(pow(a, b, m))
```

## Walkthrough
- `pow(a, b)` is exactly the same as `a ** b` — just a function form of the
  same operation.
- `pow(a, b, m)` is a **3-argument** version that computes `(a ** b) % m`
  directly, without ever building the full, possibly enormous `a ** b` value
  along the way. If `b` is very large, `a ** b` could be a number with
  thousands of digits — computing that in full just to throw most of it away
  with `% m` wastes a lot of time and memory. The 3-argument `pow()` avoids
  that entirely by working with the remainder at every step instead of the
  full number.
- The takeaway: when you need "some power, mod something," reach for
  `pow(a, b, m)` rather than `(a ** b) % m` — same answer, but built for
  exactly this situation.
