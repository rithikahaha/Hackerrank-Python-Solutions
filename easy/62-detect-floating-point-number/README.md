# 62. Detect Floating Point Number

[HackerRank link](https://www.hackerrank.com/challenges/introduction-to-regex/problem)

## What it's asking
Given `N` strings, print `True` if a string is a valid floating point
number (like `4.0`, `-1.25`, `+3.`), and `False` otherwise. Rules: it can
have an optional `+` or `-` sign, must contain exactly one decimal point,
and must have at least one digit **after** the decimal point.

## Steps
1. Build a regex pattern describing exactly what a valid floating point
   number looks like.
2. For each string, check whether it matches that pattern from start to
   end.
3. Print `True` or `False`.

## Code
```python
import re

n = int(input())
pattern = r'^[+-]?[0-9]*\.[0-9]+$'

for _ in range(n):
    s = input()
    print(bool(re.match(pattern, s)))
```

## Walkthrough
Breaking the pattern down piece by piece:
- `^` and `$` anchor the match to the **very start and end** of the string
  — without these, a match found anywhere inside a longer, invalid string
  would still count, which we don't want.
- `[+-]?` optionally matches a single `+` or `-` right at the start — the
  `?` means "zero or one of these."
- `[0-9]*` matches zero or more digits before the decimal point (zero is
  allowed, since `.5` is a valid float).
- `\.` matches a literal decimal point. It needs the backslash because a
  plain `.` in regex normally means "any character at all" — escaping it
  makes it mean an actual dot.
- `[0-9]+` requires **at least one** digit after the decimal point — the
  `+` means "one or more," unlike the `*` before it.
- `re.match(pattern, s)` checks if `s` matches this pattern, returning a
  match object if it does, or `None` if it doesn't. `bool(...)` converts
  that into an actual `True`/`False`, since a match object is treated as
  "truthy" and `None` is "falsy."
