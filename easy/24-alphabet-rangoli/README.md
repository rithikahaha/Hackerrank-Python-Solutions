# 24. Alphabet Rangoli

[HackerRank link](https://www.hackerrank.com/challenges/alphabet-rangoli/problem)

## What it's asking
Given a size `n`, print a diamond pattern made of lowercase letters. For
`n = 5`:

```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

The middle row uses all `n` letters (from `a` up to the `n`-th letter),
mirrored around `a`. Each row moving outward from the middle drops one
letter from each end, until the top and bottom rows show just the single
outermost letter.

## Steps
1. Work out each row's letters, from the *top* down to the *middle*: row `i`
   (`0` at the very top) uses letters counting down from the `n`-th letter to
   the `(n-i)`-th letter, and then back up again — a palindrome.
2. Join each row's letters with `-`, then center it within the full pattern
   width so everything lines up.
3. The pattern is symmetric top-to-bottom, so build the top half (including
   the middle row) once, then print it followed by the same rows in reverse
   (skipping the middle row the second time so it isn't repeated).

## Code
```python
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    width = 4 * size - 3

    rows = []
    for i in range(size):
        letters = [alpha[size - 1 - k] for k in range(i + 1)]
        row = letters + letters[-2::-1]
        rows.append("-".join(row).center(width, "-"))

    print("\n".join(rows + rows[-2::-1]))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
```

## Walkthrough
- `alpha[size - 1 - k]` for `k` in `0, 1, ..., i` builds a list counting
  **down** from the `size`-th letter — e.g. for `size=5`, that's `e, d, c,
  ...` — stopping after `i + 1` letters.
- `letters[-2::-1]` takes that list, drops the last item, and reverses what's
  left — mirroring it back the other way without repeating the middle
  letter. Gluing `letters + letters[-2::-1]` together gives the full
  palindrome for that row, e.g. `['e', 'd', 'c'] + ['d', 'e']` →
  `['e', 'd', 'c', 'd', 'e']`.
- `"-".join(row)` puts dashes between the letters; `.center(width, "-")`
  pads both sides with dashes so every row lines up to the same overall
  width, `4 * size - 3` (the width of the longest, middle row).
- `rows` ends up holding the top half of the pattern, from the shortest row
  (index `0`) down to the longest, middle row (index `size - 1`).
- `rows[-2::-1]` takes everything **except the last row** (the middle one)
  and reverses it — that's the bottom half, so `rows + rows[-2::-1]` gives
  the complete top-to-bottom pattern without printing the middle row twice.
