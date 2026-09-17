# 13. Hex Color Code

[HackerRank link](https://www.hackerrank.com/challenges/hex-color-code/problem)

## What it's asking
Given lines of CSS code, find every hex color code (`#fff`, `#1a2b3c`, etc.)
that's used **as a value** inside a style declaration — but skip any `#`
that's actually part of a CSS **selector**, like `#header`. In this
problem's CSS, a selector and its opening `{` typically sit on their own
lines, like:
```
#header
{
	color: #3a2eab;
}
```

## Steps
1. Keep track of whether you're currently **inside** a `{ ... }` block or
   not — selectors live outside a block, property values live inside one.
2. A line containing `{` means a block just started; a line containing `}`
   means it just ended.
3. Only search for hex colors on lines that fall **inside** a block —
   selector lines never get searched at all.

## Code
```python
import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()

    if '{' in line:
        inside_block = True
        continue
    if '}' in line:
        inside_block = False
        continue

    if inside_block:
        colors = re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', line)
        for color in colors:
            print(color)
```

## Walkthrough
- `inside_block` is a running flag remembering "am I currently between a
  `{` and its matching `}`?" It starts `False`, since the very first line is
  always a selector, not a property.
- Seeing `{` flips the flag to `True` (we've entered a block) and `continue`
  skips straight to the next line — that opening-brace line itself is never
  searched for colors, so an ID selector like `#header` never gets mistaken
  for a color value.
- Seeing `}` flips the flag back to `False` (we've left the block), so the
  next selector line also gets correctly skipped.
- Only when `inside_block` is `True` do we actually search the line for hex
  color patterns — this correctly separates "lines describing *what* to
  style" from "lines describing *how* to style it," which is exactly the
  distinction the problem cares about.
- The pattern `#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b` offers two
  alternatives, separated by `|`: a `#` followed by exactly 6 hex digits, or
  a `#` followed by exactly 3. `\b` is a **word boundary** — it matches the
  edge between "word" characters and non-word characters (like a space or
  `;`), which stops the pattern from grabbing extra digits it shouldn't
  (like the first 3 of a 6-digit code) or matching a run of more than 6.
- Trying the 6-digit alternative *first* matters: `re.findall` scans
  left to right, and at each position tries the alternatives in the order
  they're written — so a genuine 6-digit code gets matched in full, rather
  than only its first half.
- `re.findall(...)` returns every match found in the line as a list, and we
  print each one — a line can contain more than one color value.
