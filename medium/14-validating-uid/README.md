# 14. Validating UID

[HackerRank link](https://www.hackerrank.com/challenges/validating-uid/problem)

## What it's asking
Given `T` UID strings, print `Valid` or `Invalid` for each one, based on
these rules:
- Exactly 10 characters long
- Only letters and digits (no symbols or spaces)
- At least 2 uppercase letters
- At least 3 digits
- No character repeats anywhere in the string

## Steps
Check each rule one at a time — if any single one fails, the whole UID is
invalid:
1. Is it exactly 10 characters?
2. Is every character alphanumeric?
3. Does it have at least 2 uppercase letters?
4. Does it have at least 3 digits?
5. Are all the characters unique (no repeats)?

## Code
```python
import re

T = int(input())
for _ in range(T):
    uid = input()

    valid = True
    if len(uid) != 10:
        valid = False
    elif not uid.isalnum():
        valid = False
    elif len(re.findall(r'[A-Z]', uid)) < 2:
        valid = False
    elif len(re.findall(r'[0-9]', uid)) < 3:
        valid = False
    elif len(set(uid)) != len(uid):
        valid = False

    print("Valid" if valid else "Invalid")
```

## Walkthrough
- `len(uid) != 10` checks the exact length requirement directly.
- `uid.isalnum()` is a built-in string check meaning "is every character
  either a letter or a digit?" — it covers the "no symbols allowed" rule in
  one call, no regex needed.
- `re.findall(r'[A-Z]', uid)` collects every uppercase letter in the string
  into a list; checking its length tells us how many there are. The same
  idea, with `[0-9]`, counts the digits.
- `len(set(uid)) != len(uid)` is the repeat-character check: converting a
  string to a **set** automatically removes any duplicate characters. If
  the set ends up *smaller* than the original string, that means at least
  one character showed up more than once.
- Using `elif` for each check means the moment one rule fails, we stop
  checking the rest — we already know the answer is `Invalid` regardless of
  what the other rules say.
