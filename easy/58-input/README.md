# 58. Input()

[HackerRank link](https://www.hackerrank.com/challenges/input/problem)

## What it's asking
You're given two lines. The first has `x` and `y`. The second is a **Python
expression written in terms of `x`** (like `"x**2 + 3*x - 1"`), given as
text. Evaluate that expression using the actual value of `x`, and print
whether the result equals `y`.

## Steps
1. Read `x` and `y`.
2. Read the expression as text, and actually run it as Python code, using
   the `x` you just read.
3. Print whether that result matches `y`.

## Code
```python
x, y = map(int, input().split())
polynomial = eval(input())
print(polynomial == y)
```

## Walkthrough
- `eval(some_text)` takes a string containing Python code and actually
  **runs** it, returning whatever it evaluates to. So if the input line is
  the text `"x**2 + 3*x - 1"`, `eval(...)` calculates that expression using
  whatever `x` currently holds in your program.
- This problem exists to highlight something Python changed between
  versions: in Python 2, `input()` used to automatically evaluate expressions
  like this for you. In Python 3, `input()` always just gives you back the
  raw text — if you want it evaluated as code, you now have to explicitly
  wrap it in `eval()` yourself.
- `polynomial == y` compares the number `eval()` calculated against `y`, and
  `print(...)` shows whether they matched (`True` or `False`).
- Worth knowing: `eval()` is powerful because it runs *any* code you give
  it — that's fine here where the input is trusted, but it's something to be
  careful with in real programs, since you generally don't want to run
  arbitrary code from an untrusted source.
