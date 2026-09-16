# 13. Tuples

[HackerRank link](https://www.hackerrank.com/challenges/python-tuples/problem)

## What it's asking
You're given `n` numbers on one line. Put them into a **tuple** and print
`hash()` of that tuple.

## Steps
1. Read `n` (not actually needed for the logic, just tells you how many
   numbers are coming).
2. Read the numbers and convert them from text to integers.
3. Turn them into a tuple.
4. Print `hash(tuple)`.

## Code
```python
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
```

## Walkthrough
- A **tuple** looks a lot like a list — `(1, 2, 3)` instead of `[1, 2, 3]` —
  but once it's created, it can't be changed. No `.append()`, no `.sort()`,
  nothing. Lists are for data that changes; tuples are for data that's fixed.
- `map(int, input().split())` reads the line, splits it into pieces on
  spaces, and converts each piece to an integer — same pattern you've seen
  in earlier problems.
- `tuple(integer_list)` takes those numbers and locks them into a tuple.
- `hash(t)` returns a number that represents that exact tuple's value. This
  only works because tuples don't change — Python can only hash things it
  knows won't be modified later (which is also why you *can't* hash a list).
  You won't use `hash()` much day-to-day, but this problem exists specifically
  to show you tuples support it and lists don't.
