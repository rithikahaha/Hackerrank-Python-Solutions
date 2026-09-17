# 59. Python Evaluation

[HackerRank link](https://www.hackerrank.com/challenges/python-eval/problem)

## What it's asking
You're given one line of input containing an actual piece of Python code as
text (for example `print(2 + 3)`). Run it.

## Steps
1. Read the line.
2. Run it as real Python code.

## Code
```python
eval(input())
```

## Walkthrough
- `input()` reads the line as plain text — at this point it's just a string
  like `"print(2 + 3)"`, not actual code.
- `eval(...)` takes that string and executes it as if you'd typed it
  directly into your program. Since the input here is something like a
  `print(...)` call, running it produces the same output that call would
  normally produce.
- This is the simplest possible demonstration of `eval()` — it's mostly here
  so you see, in the smallest way possible, that a string of Python code and
  actually *running* that code are two different things, and `eval()` is
  the bridge between them.
- As with the previous problem, this is safe here because the input is
  trusted — running `eval()` on text from an untrusted source (like random
  user input on a real website) is a real security risk, since it would let
  someone run arbitrary code.
