# 60. Any or All

[HackerRank link](https://www.hackerrank.com/challenges/any-or-all/problem)

## What it's asking
Given a list of integers, print `True` if **both** of these hold:
1. Every number in the list is positive (greater than `0`)
2. At least one number reads the same forwards and backwards (a
   palindrome, like `121` or `7`)

Otherwise, print `False`.

## Steps
1. Read the list of numbers (keep them as text for the palindrome check).
2. Check whether every number is positive.
3. Check whether at least one number is a palindrome.
4. Print `True` only if both checks passed.

## Code
```python
n = int(input())
nums = input().split()

all_positive = all(int(x) > 0 for x in nums)
any_palindrome = any(x == x[::-1] for x in nums)

print(all_positive and any_palindrome)
```

## Walkthrough
- `all(...)` checks that **every** item in a sequence is `True` — the
  moment it finds one that isn't, it stops and returns `False`. Here,
  `int(x) > 0` checks each number is positive.
- `any(...)` checks that **at least one** item is `True` — it returns
  `True` the moment it finds a single match. Here, `x == x[::-1]` checks if
  the text reads the same reversed.
- `x[::-1]` is a slice that reverses a string — `[::-1]` means "go through
  the whole thing, but backwards." We're comparing each number's *text*
  representation to itself reversed, since checking "does this read the
  same backwards" is naturally a text operation, not a math one.
- We keep `nums` as strings (never convert the whole list to `int`) so this
  reversal trick works directly — converting to `int` first with
  `int(x) > 0` happens only inline, just for that one check.
- The final answer needs **both** conditions to hold, which is exactly what
  `and` checks.
