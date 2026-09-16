# 22. Designer Door Mat

[HackerRank link](https://www.hackerrank.com/challenges/designer-door-mat/problem)

## What it's asking
Given `N` (rows) and `M` (columns, always `3 * N`), print a door mat design
like this (for `N=9, M=27`):

```
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
-------------WELCOME-------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
```

The pattern grows from a single `.|.` at top to a full row at the middle
(which says `WELCOME` instead), then shrinks back down — like a diamond,
everything padded with `-` and centered.

## Steps
1. For the top half: for each row, repeat `.|.` a growing number of times
   (1, 3, 5, ...), then center that text within the full width using `-` as
   padding.
2. Print the middle row: `WELCOME`, centered the same way.
3. For the bottom half: repeat the same rows as the top half, but in reverse
   order.

## Code
```python
n, m = map(int, input().split())

for i in range(n // 2):
    print((".|." * (2 * i + 1)).center(m, "-"))

print("WELCOME".center(m, "-"))

for i in range(n // 2 - 1, -1, -1):
    print((".|." * (2 * i + 1)).center(m, "-"))
```

## Walkthrough
- `".|." * (2 * i + 1)` repeats the `.|.` pattern `2*i + 1` times. As `i`
  goes `0, 1, 2, ...`, that gives `1, 3, 5, ...` repeats — an odd number that
  grows each row, which is what makes the diamond shape.
- `"...".center(m, "-")` centers a piece of text within a field `m`
  characters wide, filling the empty space on both sides with `-` instead of
  spaces.
- `range(n // 2)` gives the top half's row count. Since `n` is always odd,
  `n // 2` rounds down — for `n=9` that's 4 rows above the middle, which
  matches the 4 rows shown above `WELCOME` in the example.
- `range(n // 2 - 1, -1, -1)` counts backwards from `n // 2 - 1` down to `0` —
  this replays the same `i` values as the top loop, just in reverse, so the
  bottom half mirrors the top.
