# 38. Mod Divmod

[HackerRank link](https://www.hackerrank.com/challenges/python-mod-divmod/problem)

## What it's asking
Given two integers `a` and `b`, print:
1. `a // b` (integer division)
2. `a % b` (the remainder)
3. Both of those together, as one tuple: `(a // b, a % b)`

## Steps
1. Read `a` and `b`.
2. Print the integer division.
3. Print the remainder.
4. Print both together using `divmod`.

## Code
```python
a = int(input())
b = int(input())

print(a // b)
print(a % b)
print(divmod(a, b))
```

## Walkthrough
- `a // b` and `a % b` you've already used in earlier problems — integer
  division and remainder.
- `divmod(a, b)` is a built-in function that computes **both at once** and
  hands them back together as a tuple: `(a // b, a % b)`. It exists purely
  as a convenience for when you need both values, so you're not doing the
  same division twice.
- Printing a tuple directly, like `print(divmod(a, b))`, shows it with
  parentheses and a comma, e.g. `(3, 1)` — that's just how Python displays
  tuples.
