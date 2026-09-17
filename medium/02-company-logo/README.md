# 2. Company Logo

[HackerRank link](https://www.hackerrank.com/challenges/most-commons/problem)

## What it's asking
Given a string, find the **3 most frequent characters**. Print each one
with its count, ordered by frequency (highest first) — and for characters
tied on frequency, break the tie alphabetically.

## Steps
1. Count how many times each character appears.
2. Sort the characters by count (highest first), breaking ties
   alphabetically.
3. Print the top 3.

## Code
```python
from collections import Counter

s = input()
counts = Counter(s)

for char, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:3]:
    print(char, count)
```

## Walkthrough
- `Counter(s)` counts how many times each character shows up in `s` — same
  tool from the "collections.Counter()" problem in the Easy section, applied
  to individual characters this time instead of shoe sizes.
- `sorted(..., key=...)` sorts by whatever the `key` function returns for
  each item. Here, the key is a **tuple**: `(-item[1], item[0])`, where
  `item[1]` is the count and `item[0]` is the character.
- Sorting normally goes smallest-to-largest. Negating the count
  (`-item[1]`) flips that, so the *highest* counts come first — a common
  trick for "sort descending" without having to reverse the whole sort
  afterward.
- When two items have the **same** count (so `-item[1]` ties), Python moves
  on to compare the *next* value in the tuple — `item[0]`, the character
  itself — which sorts those ties alphabetically, exactly the tie-break rule
  the problem wants.
- `[:3]` takes just the first three results after sorting — the three most
  frequent characters.
