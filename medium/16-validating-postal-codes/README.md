# 16. Validating Postal Codes

[HackerRank link](https://www.hackerrank.com/challenges/validating-postalcode/problem)

## What it's asking
Given a postal code `P`, print `True` if **both** of these hold:
1. It's a 6-digit number from `100000` to `999999` (so it can't start with
   `0`).
2. Looking at every pair of digits exactly 2 positions apart (position `i`
   and position `i+2`), at most **one** such pair is allowed to match — e.g.
   in `"523456"` no such pair matches at all (valid), while in `"121131"`,
   position 0 matches position 2 (both `1`), *and* position 3 matches
   position 5 (both `1`) — two matching pairs, which breaks the rule.

## Steps
1. Check the basic shape: exactly 6 digits, not starting with `0`.
2. Scan through the string checking, at every position, whether the digit
   two spots ahead matches it.
3. Count how many times that happens. If it's `0` or `1`, the second rule
   passes.
4. The postal code is valid only if **both** checks pass.

## Code
```python
import re

regex_integer_in_range = r"^[1-9][0-9]{5}$"
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"

P = input()

print(bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
```

## Walkthrough
- `regex_integer_in_range`: `^[1-9]` requires the first digit to be `1`
  through `9` (never `0`), then `[0-9]{5}` requires exactly 5 more digits —
  together, exactly 6 digits total, never starting with `0`.
- `regex_alternating_repetitive_digit_pair`: `(\d)` captures a single digit
  at some position. `(?=\d\1)` is a **lookahead** — it checks what comes
  *right after*, without actually consuming those characters: "any digit,
  then the *same* digit as what `(\d)` just captured" (`\1` is a
  **backreference**, meaning "whatever the first group matched"). So this
  checks: does the digit 2 positions ahead match the current one?
- The lookahead trick matters for a subtle reason: because it doesn't
  consume any characters, the regex engine only moves forward by 1 position
  after each match (since `(\d)` itself is the only part that actually
  consumed a character). That means `re.findall` can find **overlapping**
  matches — checking position 0 against 2, then position 1 against 3, then
  2 against 4, and so on, without skipping any pair. A plain (non-lookahead)
  pattern wouldn't do this correctly, since a normal match consumes
  everything it matches and the next search would start *after* it.
- `len(re.findall(...)) < 2` counts how many such matching pairs exist, and
  requires there to be fewer than 2 (so, `0` or `1`).
- Both conditions are combined with `and`, so the code only prints `True`
  when the postal code has the right shape **and** doesn't have too many
  repeating pairs.
