# 55. Exceptions

[HackerRank link](https://www.hackerrank.com/challenges/exceptions/problem)

## What it's asking
You're given `T` test cases, each with two values `a` and `b`. Print
`a // b`. But:
- If `b` is `0`, dividing by it isn't allowed — catch that error instead of
  letting the program crash, and print its error message.
- If `a` or `b` isn't actually a valid whole number, catch that error too
  and print its message.

## Steps
1. For each test case, attempt to read the two numbers and divide them.
2. If dividing by zero happens, catch it and print the error's message.
3. If the input wasn't a valid integer to begin with, catch that separately
   and print its message.

## Code
```python
T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)
```

## Walkthrough
- A `try` block lets you attempt some code that *might* fail. If it does
  fail with a matching error type, Python jumps straight to the matching
  `except` block instead of crashing the whole program.
- `ZeroDivisionError` happens specifically when you divide by `0`.
- `ValueError` happens when `int(...)` can't actually convert something into
  a number — e.g. the input has letters in it, or too few/too many values.
- `except ZeroDivisionError as e:` catches the error and stores the actual
  error object in `e`. Printing `e` directly shows Python's own built-in
  message for that error, which conveniently matches the exact wording
  HackerRank expects after `"Error Code:"`.
- This is the core pattern for handling errors gracefully: try the risky
  code, and have a specific plan for each kind of thing that could go wrong,
  rather than letting any single bad input stop the whole program.
