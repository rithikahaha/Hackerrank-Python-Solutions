# 56. Incorrect Regex

[HackerRank link](https://www.hackerrank.com/challenges/incorrect-regex/problem)

## What it's asking
You're given `T` strings, each meant to be a regex (pattern-matching)
pattern. For each one, print `True` if it's actually a valid pattern, or
`False` if it's broken.

## Steps
1. For each string, try to build a regex pattern out of it.
2. If that succeeds, print `True`.
3. If it fails, catch the error and print `False` instead of crashing.

## Code
```python
import re

T = int(input())
for _ in range(T):
    pattern = input()
    try:
        re.compile(pattern)
        print(True)
    except re.error:
        print(False)
```

## Walkthrough
- `re` is Python's module for regular expressions — patterns used to match
  or search text (like "find anything that looks like an email address").
- `re.compile(pattern)` tries to turn a plain text string into an actual,
  usable regex pattern. If the text is malformed — like unmatched brackets
  or a stray special character — Python can't build a valid pattern from it.
- Instead of crashing outright, a broken pattern raises `re.error`, a
  specific error type just for this situation. We catch it with
  `except re.error:` and print `False` in that case.
- If `re.compile(pattern)` runs without raising anything, we know the
  pattern was valid, so we print `True`.
- This is the same try/except pattern from the "Exceptions" problem, just
  applied to a different kind of failure.
