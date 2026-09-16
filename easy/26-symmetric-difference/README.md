# 26. Symmetric Difference

[HackerRank link](https://www.hackerrank.com/challenges/symmetric-difference/problem)

## What it's asking
You're given two groups of numbers. Print every number that shows up in
**exactly one** of the two groups (not both), sorted in increasing order,
one per line.

## Steps
1. Read both groups of numbers into sets.
2. Find the numbers that are in one set but not the other, on both sides.
3. Sort the result and print each number on its own line.

## Code
```python
if __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))
    n = int(input())
    set_n = set(map(int, input().split()))

    result = set_m.symmetric_difference(set_n)
    for num in sorted(result):
        print(num)
```

## Walkthrough
- `set_m.symmetric_difference(set_n)` returns every value that belongs to
  `set_m` or `set_n` but **not both** — think of it as "everything except
  what they have in common."
- Sets don't keep any particular order, so before printing we run
  `sorted(result)`, which turns the set into a list ordered from smallest to
  largest.
- The `for num in ...: print(num)` loop then prints each one on its own
  line, exactly as the problem wants.
