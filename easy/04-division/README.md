# 04. Python: Division

[HackerRank link](https://www.hackerrank.com/challenges/python-division/problem)

## What it's asking
You're given two numbers, `a` and `b`. Print two divisions:
1. Integer division (`a // b`) — drops anything after the decimal point
2. Float division (`a / b`) — keeps the decimal part

## Steps
1. Read `a` and `b` as numbers.
2. Print `a // b`.
3. Print `a / b`.

## Code
```python
if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a // b)
    print(a / b)
```

## Walkthrough
- `/` is normal division — `7 / 2` gives `3.5`.
- `//` is "floor division" — it does the division, then throws away everything
  after the decimal point, keeping only the whole number. `7 // 2` gives `3`,
  not `3.5`.
- That's really the whole problem: knowing Python has two different division
  operators and what each one keeps.
