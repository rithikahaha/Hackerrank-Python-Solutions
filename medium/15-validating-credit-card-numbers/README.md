# 15. Validating Credit Card Numbers

[HackerRank link](https://www.hackerrank.com/challenges/validating-credit-card-number/problem)

## What it's asking
Given `N` credit card numbers, print `Valid` or `Invalid` based on these
rules:
- Starts with `4`, `5`, or `6`
- Exactly 16 digits, either with no separators (`4253625879615786`) or
  grouped into four blocks of 4 with hyphens
  (`4253-6258-7961-5786`) — no other hyphen placement allowed
- No digit repeated **4 or more times in a row**, anywhere in the number

## Steps
1. Check the overall shape: right starting digit, correct length, and
   hyphens (if any) only in the standard grouped position.
2. Separately, check for any run of 4+ identical digits in a row (checking
   this on the number with hyphens removed, since a repeated run could
   otherwise be split across a hyphen).
3. Print `Valid` only if both checks pass.

## Code
```python
import re

n = int(input())
for _ in range(n):
    card = input()

    valid = True
    if not re.match(r'^[456]\d{3}(-?\d{4}){3}$', card):
        valid = False
    elif re.search(r'(\d)\1{3,}', card.replace('-', '')):
        valid = False

    print("Valid" if valid else "Invalid")
```

## Walkthrough
- `^[456]\d{3}` matches the start: one of `4`/`5`/`6`, then exactly 3 more
  digits — completing the first group of 4.
- `(-?\d{4}){3}` repeats "an optional hyphen, then exactly 4 digits" three
  more times, covering the remaining 12 digits. Because the hyphen is
  optional in **each** repeat, this allows either zero hyphens throughout,
  or hyphens in exactly the standard `XXXX-XXXX-XXXX-XXXX` positions — but
  rejects a hyphen anywhere else, since a hyphen can only appear right
  before one of these four-digit groups.
- The second check looks for repeated digits using a **backreference**:
  `(\d)` captures a single digit, and `\1` refers back to "whatever that
  first group actually matched." `\1{3,}` then requires **3 more**
  repeats of that exact same digit right after (4 total, counting the one
  `(\d)` already matched) — that's what "4 or more of the same digit in a
  row" means as a pattern.
- We run this second check on `card.replace('-', '')` — the hyphens
  stripped out — because a run of repeated digits could otherwise be split
  across a hyphen in the original text (like `1111-1111`), which would
  hide it from the pattern if the hyphens were still there.
