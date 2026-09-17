# 10. Validating Roman Numerals

[HackerRank link](https://www.hackerrank.com/challenges/validate-a-roman-number/problem)

## What it's asking
Given a string, print `True` if it's a valid Roman numeral (representing a
number from 1 to 3999, following the standard subtractive rules like `IV`
for 4 and `IX` for 9), or `False` otherwise.

## Steps
Roman numerals always list their symbols in a fixed order — thousands,
then hundreds, then tens, then ones. So the pattern needs one section per
place value, each with its own valid forms:
1. Thousands: zero to three `M`s (there's no shorthand form needed here,
   since 4000 isn't a valid input).
2. Hundreds: either a subtractive pair (`CD` for 400, `CM` for 900), or a
   normal count (`D` optionally followed by up to three `C`s, covering 0,
   100, ..., 800).
3. Tens: the same pattern, one level down (`XL`/`XC`, or `L` plus up to
   three `X`s).
4. Ones: the same pattern again (`IV`/`IX`, or `V` plus up to three `I`s).

## Code
```python
import re

regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

print(str(bool(re.match(regex_pattern, input()))))
```

## Walkthrough
- `^` and `$` anchor the pattern to the **whole** string, start to finish —
  the same anchoring idea from "Detect Floating Point Number" in the Easy
  section, making sure nothing extra sneaks in before or after a valid
  match.
- `M{0,3}` matches zero to three `M` characters directly, in a row — this
  covers thousands (`0`, `1000`, `2000`, or `3000`).
- `(CM|CD|D?C{0,3})` is the hundreds section, and it's a group offering
  three alternatives separated by `|` — only **one** of them needs to
  match:
  - `CM` — exactly 900
  - `CD` — exactly 400
  - `D?C{0,3}` — an optional `D` (500), followed by zero to three `C`s —
    covering `0`, `100`, `200`, `300` (no `D`) or `500`–`800` (with `D`)
- The tens group `(XC|XL|L?X{0,3})` and ones group `(IX|IV|V?I{0,3})` work
  exactly the same way, one place value down each time.
- `re.match(pattern, s)` checks the string against this pattern from the
  start; `bool(...)` turns the result (a match object, or `None`) into an
  actual `True`/`False`; `str(...)` converts that into the text HackerRank
  expects to see printed.
