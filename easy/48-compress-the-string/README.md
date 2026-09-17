# 48. Compress the String!

[HackerRank link](https://www.hackerrank.com/challenges/compress-the-string/problem)

## What it's asking
Given a string of digits, compress consecutive runs of the same digit into
`(count, digit)` pairs. For example, `"1222311"` becomes
`(1, 1) (3, 2) (1, 3) (2, 1)` — one `1`, then three `2`s, then one `3`, then
two `1`s.

## Steps
1. Walk through the string and group consecutive matching characters
   together.
2. For each group, record how many characters were in it and what the
   character was.
3. Print all the `(count, digit)` pairs on one line.

## Code
```python
from itertools import groupby

S = input()

result = [(len(list(group)), int(key)) for key, group in groupby(S)]
print(*result)
```

## Walkthrough
- `groupby(S)` walks through `S` and clusters together consecutive runs of
  the same character. For each run, it gives you `(key, group)`, where
  `key` is the repeated character and `group` is the run itself (as a
  mini-iterator).
- `len(list(group))` turns that run into an actual list so we can measure
  its length — that's the count for this pair.
- `int(key)` converts the repeated character (which is still text, like
  `"2"`) into an actual number, `2`.
- The list comprehension builds one `(count, digit)` tuple per run, in
  order, exactly matching the run-length structure of the original string.
- `print(*result)` unpacks the list of tuples so they print space-separated
  on a single line, rather than as one big list object.
- **Important:** `groupby` only catches characters that are *right next to*
  each other. `"11211"` would give three groups — `(2, 1)`, `(1, 2)`,
  `(2, 1)` — because the two runs of `1` aren't adjacent.
