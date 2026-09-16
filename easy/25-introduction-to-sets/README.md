# 25. Introduction to Sets

[HackerRank link](https://www.hackerrank.com/challenges/py-introduction-to-sets/problem)

## What it's asking
Given a list of numbers (plant heights), find the average of the **distinct**
values only — if a height repeats, it should only count once toward the
average.

## Steps
1. Read the list of numbers.
2. Remove duplicates.
3. Average what's left: total divided by count.

## Code
```python
def average(array):
    distinct = set(array)
    return sum(distinct) / len(distinct)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
```

## Walkthrough
- A **set** is a collection like a list, but it automatically drops
  duplicates and doesn't keep track of order. `set(array)` takes our list and
  gives back only the unique values.
- `sum(distinct)` adds up those unique values; `len(distinct)` counts how
  many there are. Dividing one by the other gives the average of the
  distinct values, which is exactly what the problem wants — repeats don't
  get counted twice.
- This is the simplest possible set problem, mostly here to introduce the
  idea: reach for a set anytime "remove duplicates" is part of what you need
  to do.
