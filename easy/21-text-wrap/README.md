# 21. Text Wrap

[HackerRank link](https://www.hackerrank.com/challenges/text-wrap/problem)

## What it's asking
Given a string and a maximum line width, wrap the text so each line is no
longer than that width — breaking at spaces, the way a word processor wraps
a paragraph.

## Steps
1. Read the string and the max width.
2. Use Python's built-in text-wrapping tool to break it into lines of that
   width.
3. Print the result.

## Code
```python
import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
```

## Walkthrough
- `textwrap` is a module in Python's standard library built specifically for
  this — you don't need to write your own wrapping logic.
- `textwrap.fill(string, max_width)` takes the text and returns it as a
  single string with line breaks (`\n`) inserted so no line exceeds
  `max_width` characters. It also has a sibling, `textwrap.wrap(...)`, which
  does the same thing but gives you back a *list* of lines instead of one
  string with `\n` in it — `.fill()` is just that list already joined
  together for you.
- This problem is really about knowing a useful built-in module exists,
  rather than practicing loops — a good reminder that Python often already
  has a tool for common text problems.
