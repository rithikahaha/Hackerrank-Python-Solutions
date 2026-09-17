# 11. Validating Phone Numbers

[HackerRank link](https://www.hackerrank.com/challenges/validating-the-phone-number/problem)

## What it's asking
Given `N` phone numbers, print `YES` or `NO` for whether each one is a
valid mobile number: exactly 10 digits, and starting with `7`, `8`, or `9`.

## Steps
1. Build a pattern describing exactly that shape: one starting digit from
   `{7, 8, 9}`, followed by exactly 9 more digits, nothing else.
2. Check each number against it.
3. Print `YES` or `NO`.

## Code
```python
import re

n = int(input())
for _ in range(n):
    number = input()
    if re.match(r'^[789]\d{9}$', number):
        print("YES")
    else:
        print("NO")
```

## Walkthrough
- `[789]` matches exactly **one** character that's either `7`, `8`, or `9` —
  a character class listing the allowed options.
- `\d{9}` requires exactly 9 more digits right after that — `{9}` is a
  repeat count, meaning "exactly 9 times."
- `^` and `$` anchor the pattern to the whole string, so nothing shorter or
  longer sneaks through — combined with the two pieces above, this only
  matches strings that are **exactly** 10 characters: one of 7/8/9,
  followed by 9 more digits, and nothing else before or after.
- `re.match(pattern, number)` checks the string against this pattern; if it
  matches, we print `"YES"`, otherwise `"NO"`.
