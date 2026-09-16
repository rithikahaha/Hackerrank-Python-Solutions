# 03. Arithmetic Operators

[HackerRank link](https://www.hackerrank.com/challenges/python-arithmetic-operators/problem)

## What it's asking
You're given two numbers, `a` and `b`. Print, on three separate lines:
1. Their sum
2. Their difference (`a - b`)
3. Their product

## Steps
1. Read `a` and `b`, converting each from text to a number.
2. Print `a + b`.
3. Print `a - b`.
4. Print `a * b`.

## Code
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a + b)
    print(a - b)
    print(a * b)
```

## Walkthrough
- Each `input()` call reads one line, so calling it twice reads two separate
  lines — one for `a`, one for `b`.
- `+`, `-`, and `*` work exactly like normal math once both values are
  numbers rather than text.
- This one's mostly here to get you comfortable with reading multiple lines
  of input — the real problems ahead build on this pattern.
