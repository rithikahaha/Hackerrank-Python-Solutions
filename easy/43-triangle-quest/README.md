# 43. Triangle Quest

[HackerRank link](https://www.hackerrank.com/challenges/python-quest-1/problem)

## What it's asking
Given `n`, print this pattern for rows `1` to `n - 1`:
```
1
22
333
4444
```
Row `i` is just the digit `i`, repeated `i` times.

## Steps
1. For each row number `i`, turn `i` into a single-digit piece of text.
2. Repeat that text `i` times.
3. Print it.

## Code
```python
for i in range(1, int(input())):
    print(str(i) * i)
```

## Walkthrough
- `str(i)` converts the number `i` into text — e.g. `str(4)` gives `"4"`.
- Multiplying a string by a number repeats it that many times:
  `"4" * 4` gives `"4444"`. This is the same trick you'd use to repeat any
  piece of text — Python lets you `*` a string just like a number, and it
  means "repeat," not "multiply the value."
- So `str(i) * i` builds exactly the row we want: the digit `i`, written out
  `i` times.
- Note the loop stops at `int(input())` — not `+ 1` like the other triangle
  problem — because HackerRank's template for this one already stops one
  short of `n`.
