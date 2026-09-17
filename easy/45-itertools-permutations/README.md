# 45. itertools.permutations()

[HackerRank link](https://www.hackerrank.com/challenges/itertools-permutations/problem)

## What it's asking
Given a string `S` and a number `k`, print every possible **ordering** of
`k` characters chosen from `S`, one per line, in alphabetical order.

## Steps
1. Sort the letters of `S` first — this makes the output come out in
   alphabetical order automatically.
2. Generate every possible ordered selection of `k` letters.
3. Print each one, glued back into a single string.

## Code
```python
from itertools import permutations

S, k = input().split()
k = int(k)

for perm in permutations(sorted(S), k):
    print("".join(perm))
```

## Walkthrough
- `permutations(iterable, k)` gives you every possible **ordered**
  arrangement of `k` items from `iterable` — order matters here, so `"AB"`
  and `"BA"` both show up separately (unlike combinations, which come next).
- It preserves the order of whatever you feed it, which is exactly why we
  sort `S` first with `sorted(S)` — that guarantees the permutations come
  out in alphabetical order too, without needing to sort the results
  afterward.
- Each permutation comes back as a tuple of individual characters, like
  `('A', 'B')`. `"".join(perm)` glues that tuple into a plain string
  `"AB"`, ready to print.
