# 07. Print Function

[HackerRank link](https://www.hackerrank.com/challenges/python-print/problem)

## What it's asking
You're given a number `n`. Print the integers from `1` to `n` **glued
together with no spaces or line breaks**, like `123456789` for `n = 9`.

## Steps
1. Read `n`.
2. Start with an empty piece of text.
3. Go through every number from `1` to `n`, turning each one into text and
   sticking it onto the end.
4. Print the final combined text once, after the loop finishes.

## Code
```python
if __name__ == '__main__':
    n = int(input())

    result = ""
    for i in range(1, n + 1):
        result += str(i)

    print(result)
```

## Walkthrough
- `range(1, n + 1)` gives `1, 2, 3, ..., n`. We need `n + 1` as the stopping
  point because `range` always stops just *before* its second value.
- `str(i)` turns the number `i` into text, since you can only glue text
  (strings) together with `+=`, not numbers and text mixed.
- `result += str(i)` means "take whatever `result` already is, and add this
  new bit of text onto the end of it." It's shorthand for
  `result = result + str(i)`.
- We only call `print()` once, after the loop is completely done, so
  everything comes out on one line with nothing in between.
