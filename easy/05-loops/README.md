# 05. Loops

[HackerRank link](https://www.hackerrank.com/challenges/python-loops/problem)

## What it's asking
You're given a number `n`. Print the square of every number from `0` up to
`n - 1`, each on its own line.

## Steps
1. Read `n`.
2. Go through every number starting at `0` and stopping just before `n`.
3. For each one, print its square (the number multiplied by itself).

## Code
```python
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i ** 2)
```

## Walkthrough
- `range(n)` generates the sequence `0, 1, 2, ..., n-1` — it stops **before**
  reaching `n`, which is a common trip-up when you're starting out.
- `for i in range(n):` means "for each number in that sequence, call it `i`,
  and run the code below once per number."
- `i ** 2` means "i to the power of 2," i.e. `i * i`. `**` is Python's
  exponent operator.
- So the loop runs once for every number from `0` to `n-1`, printing that
  number squared each time.
