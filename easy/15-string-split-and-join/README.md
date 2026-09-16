# 15. String Split and Join

[HackerRank link](https://www.hackerrank.com/challenges/python-string-split-and-join/problem)

## What it's asking
Given a line of text with words separated by spaces, join those same words
back together using `-` instead of spaces.

## Steps
1. Split the string wherever there's a space, giving you a list of words.
2. Glue those words back together, this time with `-` in between instead of
   a space.

## Code
```python
def split_and_join(line):
    return "-".join(line.split(" "))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
```

## Walkthrough
- `line.split(" ")` breaks the string apart everywhere it finds a space,
  giving you a list like `["this", "is", "a", "string"]`.
- `"-".join(...)` does the opposite of `split` — it takes a list of pieces
  and glues them into one string, putting whatever's in front of `.join`
  (here, `"-"`) between each piece.
- Put together: `"-".join(line.split(" "))` reads as "split on spaces, then
  join back with dashes." This split-then-join pattern shows up constantly
  once you start manipulating text.
