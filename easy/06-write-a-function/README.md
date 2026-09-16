# 06. Write a Function

[HackerRank link](https://www.hackerrank.com/challenges/write-a-function/problem)

## What it's asking
Write a function that takes a `year` and returns `True` if it's a leap year,
`False` otherwise.

The leap year rule:
- Divisible by 4 → leap year...
- ...**unless** it's also divisible by 100 → then it's *not* a leap year...
- ...**unless** it's *also* divisible by 400 → then it *is* a leap year after all.

(e.g. 2000 was a leap year, but 1900 was not.)

## Steps
1. Start by assuming it's not a leap year.
2. If the year divides evenly by 4, tentatively mark it as a leap year.
3. But if it *also* divides evenly by 100, undo that — it's not a leap year.
4. Unless it *also* divides evenly by 400 — in that case it is one after all.
5. Return whatever you landed on.

## Code
```python
def is_leap(year):
    leap = False

    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True

    return leap


year = int(input())
print(is_leap(year))
```

## Walkthrough
- `year % 4 == 0` checks "does 4 divide into year with nothing left over?" —
  that's what "divisible by 4" means in code.
- The nested `if` statements mirror the rule exactly: each exception only
  gets checked once the outer condition is already true, which is why they're
  indented inside one another.
- `leap` is just a variable holding `True` or `False` as we update our answer
  step by step, then we hand it back with `return leap`.
- This problem is really about practicing **functions** — a function is a
  named, reusable block of code that takes an input (`year`) and gives back
  an output (`return leap`), so you can call it whenever you need it.
